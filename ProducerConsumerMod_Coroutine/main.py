from producer import Producer
from consumer import Consumer
import asyncio
from asyncio import Lock
from asyncio import Queue


async def run():
    q = Queue(maxsize=1000)
    producer_lock = Lock()
    consumer_lock = Lock()
    producer_workers = 3
    consumer_workers = 3
    producer_coroutines = (Producer(i, q, producer_lock) for i in range(producer_workers))
    consumer_coroutines = (Consumer(i, q, consumer_lock) for i in range(consumer_workers))
    await asyncio.gather(*producer_coroutines, *consumer_coroutines)


if __name__ == '__main__':
    asyncio.run(run())
