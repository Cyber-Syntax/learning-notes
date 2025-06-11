import time
import threading
import multiprocessing
import asyncio
import concurrent.futures
from queue import Queue

# Mock configuration
NUM_TASKS = 5
DELAY_PER_TASK = 0.5  # Seconds


def mock_github_install(task_id):
    """Mock installation function simulating network delay"""
    start = time.perf_counter()
    time.sleep(DELAY_PER_TASK)  # Simulate I/O bound work
    end = time.perf_counter()
    return task_id, start, end


async def async_mock_github_install(task_id):
    """Async version of mock installation"""
    start = time.perf_counter()
    await asyncio.sleep(DELAY_PER_TASK)  # Non-blocking delay
    end = time.perf_counter()
    return task_id, start, end


def sequential_install():
    """Sequential execution (baseline)"""
    results = []
    for i in range(NUM_TASKS):
        results.append(mock_github_install(i))
    return results


def threading_install():
    """Threading execution"""
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(mock_github_install, i) for i in range(NUM_TASKS)]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    return results


def multiprocessing_install():
    """Multiprocessing execution"""
    results = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(mock_github_install, i) for i in range(NUM_TASKS)]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    return results


async def asyncio_install():
    """Asyncio execution"""
    tasks = [async_mock_github_install(i) for i in range(NUM_TASKS)]
    return await asyncio.gather(*tasks)


def run_and_print(method_name, install_func):
    """Run installation method and print timing results"""
    print(f"\n{method_name}:\n{'=' * 40}")
    start_time = time.perf_counter()

    if method_name == "Asyncio":
        results = asyncio.run(install_func())
    else:
        results = install_func()

    total_time = time.perf_counter() - start_time

    # Print individual task results
    for task_id, start, end in sorted(results):
        print(
            f"Task {task_id}: Start={start - start_time:.3f}s, End={end - start_time:.3f}s"
        )

    # Print summary
    print(f"\nTotal time: {total_time:.3f}s")
    print(f"Expected minimum: {DELAY_PER_TASK:.3f}s")
    print(f"Efficiency: {DELAY_PER_TASK * NUM_TASKS / total_time:.1f}x")


if __name__ == "__main__":
    print(f"Testing with {NUM_TASKS} tasks ({DELAY_PER_TASK}s delay each)\n")

    # Run all methods
    run_and_print("Sequential", sequential_install)
    run_and_print("Threading", threading_install)
    run_and_print("Multiprocessing", multiprocessing_install)
    run_and_print("Asyncio", asyncio_install)
