from asyncio import Lock
from asyncio import Queue
import asyncio


async def Consumer(num: int, q: Queue, consumer_lock: Lock):
    print(f"{num} 开始消费数据\n")
    while 1:
        qsize = await asyncio.to_thread(lambda x: x.qsize(), q)
        if qsize != 0:
            body = await q.get()
            async with consumer_lock:
                print(f"由消费者{num}消费的{body}出队列\n")
            await asyncio.sleep(0.001)
