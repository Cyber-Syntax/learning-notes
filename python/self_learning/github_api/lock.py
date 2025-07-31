import threading

concurrent_counter = 0


def increment_without_lock():
    global concurrent_counter
    concurrent_counter += 1


def increment_with_lock(lock):
    global concurrent_counter
    for _ in range(10):
        with lock:
            concurrent_counter += 1


def run_test(use_lock=False):
    global concurrent_counter
    concurrent_counter = 0
    threads = []
    lock = threading.Lock() if use_lock else None

    for _ in range(5):
        if use_lock:
            t = threading.Thread(target=increment_with_lock, args=(lock,))
        else:
            t = threading.Thread(target=increment_without_lock)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(
        f"{'With' if use_lock else 'Without'} lock final counter value: {concurrent_counter}"
    )

    # Output:
    # With lock final counter value: 50
    # Without lock final counter value: 5


if __name__ == "__main__":
    run_test(use_lock=True)
    run_test(use_lock=False)
