## Benchmark results
# asyncio : # Took 0.9000923823671959 seconds on average (n=30)
# multiprocessing : # Took 0.7238470940335294 seconds on average (n=30)
# threading : # Took 3.45687337996654 seconds on average (n=30)

####
#  Multiprocessing
####

# # SuperFastPython.com
# # example of benchmarking many small blocking calls with processes
# import time
# from multiprocessing import Process
#
# # fixed duration task
# def work():
#     # lots of short blocking calls
#     for i in range(10000):
#         time.sleep(0)
#
# # main program
# def main():
#     # record the start time
#     time_start = time.perf_counter()
#     # create many tasks for concurrent execution
#     tasks = [Process(target=work) for _ in range(100)]
#     # start all tasks
#     for task in tasks:
#         task.start()
#     # block and wait for all tasks to complete
#     for task in tasks:
#         task.join()
#     # record the end time
#     time_end = time.perf_counter()
#     # calculate and report the duration
#     time_duration = time_end - time_start
#     print(f'>took {time_duration} seconds')
#     # return the duration
#     return time_duration
#
# # protect the entry point
# if __name__ == '__main__':
#     # number of repeats
#     n_repeat = 30
#     # collect results
#     results = [main() for _ in range(n_repeat)]
#     # calculate the average
#     time_avg = sum(results) / n_repeat
#     # report average
#     print(f'Took {time_avg} seconds on average (n={n_repeat})')
#
# Output multiprocessing:
# Took 0.7553373341668096 seconds on average (n=30)
# Took 0.7238470940335294 seconds on average (n=30)


####
# Threading
####

# # SuperFastPython.com
# # example of benchmarking many small blocking calls with threads
# import time
# from threading import Thread

# # fixed duration task
# def work():
#     # lots of short blocking calls
#     for i in range(10000):
#         time.sleep(0)

# # main program
# def main():
#     # record the start time
#     time_start = time.perf_counter()
#     # create many tasks for concurrent execution
#     tasks = [Thread(target=work) for _ in range(100)]
#     # start all tasks
#     for task in tasks:
#         task.start()
#     # block and wait for all tasks to complete
#     for task in tasks:
#         task.join()
#     # record the end time
#     time_end = time.perf_counter()
#     # calculate and report the duration
#     time_duration = time_end - time_start
#     print(f'>took {time_duration} seconds')
#     # return the duration
#     return time_duration

# # protect the entry point
# if __name__ == '__main__':
#     # number of repeats
#     n_repeat = 30
#     # collect results
#     results = [main() for _ in range(n_repeat)]
#     # calculate the average
#     time_avg = sum(results) / n_repeat
#     # report average
#     print(f'Took {time_avg} seconds on average (n={n_repeat})')

# Output: threading:
# Took 3.45687337996654 seconds on average (n=30)


####
# Threading
####

# SuperFastPython.com
# example of benchmarking many small blocking calls with coroutines
import time
import asyncio


# fixed duration task
async def work():
    # lots of short blocking calls
    for i in range(10000):
        await asyncio.sleep(0)  # use asyncio.sleep to yield control


# main program
async def main():
    # record the start time
    time_start = time.perf_counter()
    # create many tasks for concurrent execution
    tasks = [asyncio.create_task(work()) for _ in range(100)]
    # wait for all tasks to be done
    _ = await asyncio.gather(*tasks)
    # record the end time
    time_end = time.perf_counter()
    # calculate and report the duration
    time_duration = time_end - time_start
    print(f">took {time_duration} seconds")
    # return the duration
    return time_duration


# protect the entry point
if __name__ == "__main__":
    # number of repeats
    n_repeat = 30
    # collect results
    results = [asyncio.run(main()) for _ in range(n_repeat)]
    # calculate the average
    time_avg = sum(results) / n_repeat
    # report average
    print(f"Took {time_avg} seconds on average (n={n_repeat})")

    # #Output async coroutine:
    # Took 0.9000923823671959 seconds on average (n=30)
