import os, subprocess
from datetime import datetime

# Directories
dirs_to_backup = '/home/developer/Documents/'
backup_folder = '/home/developer/Documents/backup-for-cloud'

# Encryption password
key = 'password'

# Timestamp
now = datetime.now()
date = now.strftime("%d-%m-%Y")

# Backup time
days_between_backups = 30

def compress_backup_dirs():
    # tar --exclude='test/exclude' -cJf test.tar.xz test       
    os_cmd = ["tar", "-cJf", f"{backup_folder}/{date}.tar.xz", "--exclude-from", f"{backup_folder}/ignore.txt", dirs_to_backup]
    subprocess.call(" ".join(os_cmd), shell=True)

def encrypt_backup_dirs():
    try:
        os_cmd = ["openssl", "aes-256-cbc","-a", "-pbkdf2", "-salt", "-in", f"{backup_folder}/{date}.tar.xz", "-out", f"{backup_folder}/{date}.tar.xz.enc", "-k", key]
        subprocess.call(" ".join(os_cmd), shell=True)   
    except Exception as e:
        print(f"Error encrypting file: {e}")
        return False       

compress_backup_dirs()
encrypt_backup_dirs()
