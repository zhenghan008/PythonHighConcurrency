import asyncio
from asyncio import Semaphore
from concurrent.futures import ProcessPoolExecutor
import functools
import os


async def print_test(body: str, _sem: Semaphore):
    async with _sem:
        print(f"body: {body}")
        await asyncio.sleep(0.0001)


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
    _fun = functools.partial(execute, _workers=100, _s=10)
    with ProcessPoolExecutor(max_workers=max_workers) as _pool:
        _pool.map(_fun, range(max_workers))


if __name__ == '__main__':
    main()
