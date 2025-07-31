# import asyncio

# semaphore = asyncio.Semaphore(2)

# async def worker(num):
#     async with semaphore:
#         print(f"Worker {num} is running")
#         await asyncio.sleep(2)
#         print(f"Worker {num} done")

# async def main():
#     tasks = [worker(i) for i in range(5)]
#     await asyncio.gather(*tasks)

# asyncio.run(main())

# Output when semaphore is set to 3 `asyncio.Semaphore(3)`
# Worker 0 is running
# Worker 1 is running
# Worker 2 is running
# Worker 0 done
# Worker 1 done
# Worker 2 done
# Worker 3 is running
# Worker 4 is running
# Worker 3 done
# Worker 4 done

# Output when semaphore is set to 2 `asyncio.Semaphore(2)`
# Worker 0 is running
# Worker 1 is running
# Worker 0 done
# Worker 1 done
# Worker 2 is running
# Worker 3 is running
# Worker 2 done
# Worker 3 done
# Worker 4 is running
# Worker 4 done

import threading
import time

# Create a semaphore allowing up to 3 concurrent accesses
semaphore = threading.Semaphore(3)

def worker(num):
    with semaphore:
        print(f"Worker {num} accessing resource")
        time.sleep(2)
        print(f"Worker {num} done")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
    
# Output when semaphore 3 `threading.Semaphore(3)`
# Worker 0 accessing resource
# Worker 1 accessing resource
# Worker 2 accessing resource
# Worker 0 done
# Worker 3 accessing resource
# Worker 1 done
# Worker 4 accessing resource
# Worker 2 done
# Worker 3 done
# Worker 4 done
