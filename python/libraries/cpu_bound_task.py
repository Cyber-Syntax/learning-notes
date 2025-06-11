import time
import threading
import multiprocessing
import asyncio
import concurrent.futures


# CPU-bound task: Calculate large factorial
def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# --- Sequential ---
def sequential():
    for i in range(5):
        calculate_factorial(50000)


# --- Threading ---
def threading_approach():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(calculate_factorial, [50000] * 5)


# --- Multiprocessing ---
def multiprocessing_approach():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(calculate_factorial, [50000] * 5)


# --- Asyncio ---
async def async_calculate_factorial(n):
    # Note: This will block the event loop!
    return calculate_factorial(n)


async def asyncio_approach():
    tasks = [async_calculate_factorial(50000) for _ in range(5)]
    await asyncio.gather(*tasks)


# Benchmark function
def benchmark(func, name):
    start = time.perf_counter()
    func()
    elapsed = time.perf_counter() - start
    print(f"{name}: {elapsed:.2f} seconds")


if __name__ == "__main__":
    print("CPU-Bound Task Benchmark (Factorial Calculation):")
    benchmark(sequential, "Sequential")
    benchmark(threading_approach, "Threading")
    benchmark(multiprocessing_approach, "Multiprocessing")

    # Special handling for asyncio
    start = time.perf_counter()
    asyncio.run(asyncio_approach())
    elapsed = time.perf_counter() - start
    print(f"Asyncio: {elapsed:.2f} seconds")
