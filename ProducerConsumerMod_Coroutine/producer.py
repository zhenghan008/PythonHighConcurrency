from asyncio import Lock
from asyncio import Queue
import asyncio

i = 0


async def Producer(num: int, q: Queue, producer_lock: Lock):
    global i
    print(f"{num} 开始生产数据\n")
    while 1:
        if i > 10000:
            break
        qsize = await asyncio.to_thread(lambda x: x.qsize(), q)
        if qsize == 0:
            await q.put(i)
            async with producer_lock:
                print(f"由生产者{num}生产的{i}进入队列\n")
                i += 1
        await asyncio.sleep(0.001)
