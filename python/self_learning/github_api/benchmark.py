import asyncio
from concurrent.futures import ThreadPoolExecutor
import threading
import time

# Example CPU-bound task (sum of squares)
def cpu_bound_task(n):
    return sum(i * i for i in range(n))

# Wrapper to run cpu_bound_task in a thread.Thread
def thread_worker(n, results, index):
    results[index] = cpu_bound_task(n)

# Async wrapper for cpu_bound_task using asyncio.to_thread (Python 3.9+)
async def async_task(n):
    return await asyncio.to_thread(cpu_bound_task, n)

async def benchmark_asyncio(n_tasks, task_size):
    start = time.perf_counter()
    tasks = [async_task(task_size) for _ in range(n_tasks)]
    results = await asyncio.gather(*tasks)
    duration = time.perf_counter() - start
    print(f"asyncio.to_thread: {duration:.4f} seconds")
    return results

def benchmark_threadpoolexecutor(n_tasks, task_size, workers=4):
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(cpu_bound_task, [task_size]*n_tasks))
    duration = time.perf_counter() - start
    print(f"ThreadPoolExecutor with {workers} workers: {duration:.4f} seconds")
    return results

def benchmark_thread(n_tasks, task_size):
    start = time.perf_counter()
    threads = []
    results = [None] * n_tasks
    for i in range(n_tasks):
        t = threading.Thread(target=thread_worker, args=(task_size, results, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    duration = time.perf_counter() - start
    print(f"Threading.Thread: {duration:.4f} seconds")
    return results

def main():
    n_tasks = 10
    task_size = 10**7

    print(f"Running benchmark with {n_tasks} tasks, task size {task_size}")

    # Benchmark Threading.Thread
    benchmark_thread(n_tasks, task_size)

    # Benchmark ThreadPoolExecutor
    benchmark_threadpoolexecutor(n_tasks, task_size)

    # Benchmark asyncio using asyncio.to_thread
    asyncio.run(benchmark_asyncio(n_tasks, task_size))
    
    # ## Results:
    #     Threading.Thread: 5.4255 seconds
    #     ThreadPoolExecutor with 4 workers: 5.1447 seconds
    #     asyncio.to_thread: 5.3937 seconds


if __name__ == "__main__":
    main()