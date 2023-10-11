import asyncio
import time
from asyncio import Semaphore, to_thread
from threading import Lock
from concurrent.futures import ProcessPoolExecutor
import functools
import os
import random

work_path = os.path.abspath(os.path.dirname(__file__))
lock = Lock()


async def p_g():
    while 1:
        for i in range(random.randint(100, 10000)):
            yield i
            await asyncio.sleep(0.0001)
        # time.sleep(random.randint(1, 5))


def write_to_file(body: str, lock: Lock):
    with lock:
        with open(work_path + "/test.txt", "a") as f:
            f.write(body)


async def print_test(body: str, _sem: Semaphore):
    async for each in p_g():
        async with _sem:
            await to_thread(write_to_file, f"each: {each}, body: {body}\r\n", lock)
            # print(f"body: {body}\r\n")
            # print(f"each: {each}, body: {body}\r\n")
            # await asyncio.sleep(0.00001)


async def run(i: int, _workers: int, _s: int):
    _sem = Semaphore(_s)
    print(f"这是属于进程{i}的协程")
    _coroutines = (print_test(str(i), _sem) for i in range(_workers))
    await asyncio.gather(*_coroutines)


def execute(i: int, _workers: int, _s: int):
    asyncio.run(run(i, _workers, _s))


def main():
    max_workers = os.cpu_count()
    # print(f"max_workers: {max_workers}")
    _fun = functools.partial(execute, _workers=100, _s=50)
    with ProcessPoolExecutor() as _pool:
        _pool.map(_fun, range(max_workers))


if __name__ == '__main__':
    main()
