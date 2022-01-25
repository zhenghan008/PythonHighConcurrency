import time
from threading import Lock
from queue import Queue


def Consumer(num: int, _q: Queue, _consumer_lock: Lock):
    print(f"{num} 开始消费数据\n")
    while 1:
        if _q.qsize() != 0:
            body = _q.get()
            with _consumer_lock:
                print(f"由消费者{num}消费的{body}出队列\n")
            time.sleep(0.001)


