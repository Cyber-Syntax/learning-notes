from __future__ import unicode_literals
import time
import sys
import threading
import random
import concurrent.futures
import os
import shutil
from abc import ABC, abstractmethod

# Status constants
STATUS_OK = 0
STATUS_FAILED = 1
STATUS_ALREADY_EXISTS = 2
STATUS_MIRROR = 3
STATUS_DRPM = 4

# Utility class for terminal operations
class util:
    @staticmethod
    def _terminal_messenger(action, msg, fo):
        if action == "write_flush":
            fo.write(msg)
            fo.flush()

def _term_width():
    """Get terminal width"""
    return shutil.get_terminal_size((80, 20)).columns

def format_number(number):
    """Format number to human readable string with units"""
    if number is None or number == 0:
        return '0'
    if number < 1000:
        return '%d' % number
    elif number < 1000000:
        return '%.1fK' % (number/1000)
    else:
        return '%.1fM' % (number/1000000)

def format_time(seconds):
    """Format time duration to MM:SS"""
    if seconds is None or seconds <= 0:
        return '--:--'
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return '%02d:%02d' % (minutes, seconds)

class DownloadProgress(ABC):
    """Abstract base class for download progress tracking"""
    
    @abstractmethod
    def start(self, total_files, total_size, total_drpms=0):
        pass
        
    @abstractmethod
    def progress(self, payload, done):
        pass
        
    @abstractmethod
    def end(self, payload, status, err_msg):
        pass

class AsyncMultiFileProgressMeter(DownloadProgress):
    """Asynchronous multi-file download progress meter with individual progress bars"""

    STATUS_2_STR = {
        STATUS_OK: 'COMPLETED',
        STATUS_FAILED: 'FAILED',
        STATUS_ALREADY_EXISTS: 'SKIPPED',
        STATUS_MIRROR: 'MIRROR',
        STATUS_DRPM: 'DRPM',
    }

    def __init__(self, fo=sys.stderr, update_period=0.1):
        super().__init__()
        self.fo = fo
        self.update_period = update_period
        self.isatty = sys.stdout.isatty()
        
        # Download state - keyed by file ID
        self.files = {}  # file_id -> {payload, status, progress, start_time, end_time, error}
        self.total_files = 0
        self.total_size = 0
        self.completed_files = 0
        
        # Threading control
        self.lock = threading.Lock()
        self.stop_event = threading.Event()
        self.thread = None
        self.file_counter = 0

    def message(self, msg):
        util._terminal_messenger('write_flush', msg, self.fo)

    def _get_file_name(self, payload):
        """Extract readable file name from URL"""
        url = str(payload.url)
        if '/' in url:
            return url.split('/')[-1]
        return url

    def start(self, total_files, total_size, total_drpms=0):
        # Stop existing thread if running
        if self.thread and self.thread.is_alive():
            self.stop_event.set()
            self.thread.join(timeout=0.1)
        
        self.stop_event.clear()
        
        with self.lock:
            self.total_files = total_files
            self.total_size = total_size
            self.completed_files = 0
            self.files = {}
            self.file_counter = 0

        if total_files == 0:
            self.stop_event.set()
            return

        # Clear screen and position cursor
        if self.isatty:
            self.message('\033[2J\033[H')  # Clear screen and move to top
            self.message('Starting downloads...\n\n')

        # Start update thread
        self.thread = threading.Thread(target=self._update_loop)
        self.thread.daemon = True
        self.thread.start()

    def _update_loop(self):
        while not self.stop_event.is_set():
            with self.lock:
                if self.stop_event.is_set():
                    break
                self._update_display()
            time.sleep(self.update_period)

    def progress(self, payload, done):
        file_id = id(payload)
        
        with self.lock:
            if file_id not in self.files:
                self.file_counter += 1
                self.files[file_id] = {
                    'payload': payload,
                    'status': 'downloading',
                    'progress': 0,
                    'start_time': time.time(),
                    'end_time': None,
                    'error': None,
                    'display_name': f"{self.file_counter}. {self._get_file_name(payload)}"
                }
            
            self.files[file_id]['progress'] = int(done)

    def end(self, payload, status, err_msg):
        file_id = id(payload)
        
        with self.lock:
            if file_id in self.files:
                self.files[file_id]['end_time'] = time.time()
                self.files[file_id]['progress'] = payload.download_size
                
                if status == STATUS_OK:
                    self.files[file_id]['status'] = 'completed'
                elif status == STATUS_FAILED:
                    self.files[file_id]['status'] = 'failed'
                    self.files[file_id]['error'] = err_msg
                else:
                    self.files[file_id]['status'] = self.STATUS_2_STR.get(status, 'unknown')
                
                self.completed_files += 1
                
                # Check if all files are done
                if self.completed_files >= self.total_files:
                    self.stop_event.set()

    def _update_display(self):
        if not self.isatty or not self.files:
            return

        # Move cursor to start of download area
        self.message('\033[3;1H')  # Move to line 3, column 1
        
        # Display each file's progress
        for file_id, file_info in sorted(self.files.items(), key=lambda x: x[1]['display_name']):
            self._display_file_progress(file_info)
        
        # Display summary
        self._display_summary()
        
        # Clear any remaining lines
        self.message('\033[K')  # Clear to end of line

    def _display_file_progress(self, file_info):
        payload = file_info['payload']
        status = file_info['status']
        progress = file_info['progress']
        display_name = file_info['display_name']
        start_time = file_info['start_time']
        
        total_size = payload.download_size
        
        # Calculate progress percentage
        if total_size > 0:
            pct = min(int(progress * 100 / total_size), 100)
        else:
            pct = 0
        
        # Calculate speed and ETA
        now = time.time()
        elapsed = now - start_time
        if elapsed > 0 and progress > 0:
            speed = progress / elapsed
            if speed > 0 and total_size > progress:
                eta = (total_size - progress) / speed
                eta_str = format_time(eta)
            else:
                eta_str = '00:00'
            speed_str = format_number(speed) + 'B/s'
        else:
            speed_str = '---B/s'
            eta_str = '--:--'
        
        # Create progress bar
        bar_width = 30
        if pct > 0:
            filled = int(bar_width * pct / 100)
            bar = '█' * filled + '░' * (bar_width - filled)
        else:
            bar = '░' * bar_width
        
        # Status indicator
        if status == 'completed':
            status_icon = '✓'
            status_color = '\033[32m'  # Green
        elif status == 'failed':
            status_icon = '✗'
            status_color = '\033[31m'  # Red
        elif status == 'downloading':
            status_icon = '↓'
            status_color = '\033[33m'  # Yellow
        else:
            status_icon = '?'
            status_color = '\033[37m'  # White
        
        reset_color = '\033[0m'
        
        # Format the line
        size_info = f"{format_number(progress)}/{format_number(total_size)}"
        
        # Truncate filename if too long
        max_name_length = 40
        if len(display_name) > max_name_length:
            display_name = display_name[:max_name_length-3] + '...'
        
        line = f"{status_color}{status_icon}{reset_color} {display_name:<{max_name_length}} [{bar}] {pct:3d}% {size_info:>12} {speed_str:>8} ETA {eta_str}"
        
        # Add error message if failed
        if status == 'failed' and file_info.get('error'):
            line += f" - {file_info['error']}"
        
        self.message(line + '\033[K\n')  # Clear to end of line and add newline

    def _display_summary(self):
        # Calculate totals
        total_downloaded = sum(f['progress'] for f in self.files.values())
        overall_pct = int(total_downloaded * 100 / self.total_size) if self.total_size > 0 else 0
        
        # Count by status
        downloading = sum(1 for f in self.files.values() if f['status'] == 'downloading')
        completed = sum(1 for f in self.files.values() if f['status'] == 'completed')
        failed = sum(1 for f in self.files.values() if f['status'] == 'failed')
        
        # Summary line
        summary = f"\n{'─' * 80}\n"
        summary += f"Overall: {completed}/{self.total_files} completed, {failed} failed, {downloading} active"
        summary += f" | Total: {format_number(total_downloaded)}/{format_number(self.total_size)} ({overall_pct}%)\n"
        
        self.message(summary)

    def download_files(self, payloads):
        """Download multiple files concurrently"""
        if not payloads:
            return
            
        # Start progress meter first
        total_size = sum(p.download_size for p in payloads)
        self.start(len(payloads), total_size)
        
        # Create thread pool with max workers
        max_workers = min(len(payloads), 8)
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all downloads immediately - they start concurrently
            futures = [executor.submit(self._download_file, payload) for payload in payloads]
            
            # Wait for all to complete
            concurrent.futures.wait(futures)
        
        # Stop the progress meter
        self.stop_event.set()
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
        
        # Final display
        with self.lock:
            self._update_display()
        
        # Show final results
        if self.isatty:
            self.message('\n\nDownload Summary:\n')
            for file_info in sorted(self.files.values(), key=lambda x: x['display_name']):
                status = file_info['status']
                name = file_info['display_name']
                if status == 'completed':
                    elapsed = file_info['end_time'] - file_info['start_time']
                    speed = file_info['payload'].download_size / elapsed if elapsed > 0 else 0
                    self.message(f"✓ {name} - {format_time(elapsed)} ({format_number(speed)}B/s)\n")
                elif status == 'failed':
                    error = file_info.get('error', 'Unknown error')
                    self.message(f"✗ {name} - FAILED: {error}\n")

    def _download_file(self, payload):
        """Simulate downloading a file with random progress updates"""
        downloaded = 0
        total = payload.download_size
        chunks = random.randint(20, 40)  # Variable number of chunks per file
        
        # Add small random start delay to make concurrency visible
        time.sleep(random.uniform(0.1, 0.5))
        
        for i in range(chunks):
            if self.stop_event.is_set():
                break
                
            # Variable chunk sizes for realistic behavior
            remaining = total - downloaded
            if i == chunks - 1:  # Last chunk
                chunk = remaining
            else:
                max_chunk = remaining // (chunks - i)
                chunk = random.randint(max_chunk // 3, max_chunk)
                chunk = min(chunk, remaining)
            
            downloaded += chunk
            self.progress(payload, downloaded)
            
            # Variable delays to simulate network conditions
            delay = random.uniform(1.01, 0.01)
            time.sleep(delay)
            
        # Ensure we complete the download
        if downloaded < total:
            self.progress(payload, total)
            
        # Random success/failure (mostly success)
        if random.random() > 0.15:  # 85% success rate
            self.end(payload, STATUS_OK, "")
        else:
            errors = ["Connection timeout", "Network unreachable", "Server error 503", "Disk full"]
            self.end(payload, STATUS_FAILED, random.choice(errors))

# Test simulation with truly concurrent downloads
if __name__ == '__main__':
    from collections import namedtuple

    print("Multi-file Concurrent Download Progress Demo")
    print("=" * 50)
    
    # Create fake payloads with realistic names and varied sizes
    FakePayload = namedtuple('FakePayload', ['download_size', 'url'])
    payloads = [
        FakePayload(1024*1024*25, "https://releases.ubuntu.com/22.04/ubuntu-22.04-desktop-amd64.iso"),
        FakePayload(1024*1024*35, "https://archlinux.org/iso/2023.08.01/archlinux-2023.08.01-x86_64.iso"),
        FakePayload(1024*1024*15, "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.1.0-amd64-netinst.iso"),
        FakePayload(1024*1024*45, "https://download.fedoraproject.org/pub/fedora/linux/releases/38/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-38-1.6.iso"),
        FakePayload(1024*1024*20, "https://cdimage.kali.org/kali-2023.3/kali-linux-2023.3-installer-amd64.iso"),
        FakePayload(1024*1024*30, "https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso"),
        FakePayload(1024*1024*18, "https://mirror.alpinelinux.org/alpine/v3.18/releases/x86_64/alpine-standard-3.18.3-x86_64.iso")
    ]

    # Create progress meter
    meter = AsyncMultiFileProgressMeter(update_period=0.1)
    
    # Start all downloads concurrently
    start_time = time.time()
    meter.download_files(payloads)
    end_time = time.time()
    
    print(f"\nAll downloads completed in {end_time - start_time:.1f} seconds!")