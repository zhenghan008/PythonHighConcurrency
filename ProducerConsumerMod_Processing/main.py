from concurrent.futures import ProcessPoolExecutor
from producer import Producer
from consumer import Consumer
from multiprocessing import Manager
import functools


def run():
    q = Manager().Queue(maxsize=1000)
    producer_lock = Manager().Lock()
    consumer_lock = Manager().Lock()
    producer_workers = 3
    consumer_workers = 3
    producer_pool = ProcessPoolExecutor(max_workers=producer_workers)
    consumer_pool = ProcessPoolExecutor(max_workers=consumer_workers)
    _Producer = functools.partial(Producer, q=q, producer_lock=producer_lock)
    _Consumer = functools.partial(Consumer, q=q, consumer_lock=consumer_lock)
    producer_pool.map(_Producer, range(producer_workers))
    consumer_pool.map(_Consumer, range(consumer_workers))


if __name__ == '__main__':
    run()
