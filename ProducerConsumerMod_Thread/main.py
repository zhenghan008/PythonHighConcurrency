from concurrent.futures import ThreadPoolExecutor
from producer import Producer
from consumer import Consumer
from threading import Lock
from queue import Queue
import functools


def run():
    q = Queue(maxsize=1000)
    producer_lock = Lock()
    consumer_lock = Lock()
    producer_workers = 3
    consumer_workers = 3
    producer_pool = ThreadPoolExecutor(max_workers=producer_workers)
    consumer_pool = ThreadPoolExecutor(max_workers=consumer_workers)
    _Producer = functools.partial(Producer, _q=q, _producer_lock=producer_lock)
    _Consumer = functools.partial(Consumer, _q=q, _consumer_lock=consumer_lock)
    producer_pool.map(_Producer, range(producer_workers))
    consumer_pool.map(_Consumer, range(consumer_workers))


if __name__ == '__main__':
    run()
