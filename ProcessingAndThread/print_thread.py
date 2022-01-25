from threading import Lock
from concurrent.futures import (ProcessPoolExecutor, ThreadPoolExecutor)
import time
import functools
import os


def print_test(body: str, lock: Lock):
    with lock:
        print(f"body: {body}")
    time.sleep(0.0001)


def run(i: int, _workers: int):
    print(f"这是属于进程{i}的线程")
    lock = Lock()
    _fun = functools.partial(print_test, lock=lock)
    with ThreadPoolExecutor(max_workers=10) as pool:
        pool.map(_fun,  range(_workers))


def main():
    max_workers = os.cpu_count()
    _fun = functools.partial(run, _workers=100)
    with ProcessPoolExecutor(max_workers=max_workers) as _pool:
        _pool.map(_fun,  range(max_workers))


if __name__ == '__main__':
    main()
