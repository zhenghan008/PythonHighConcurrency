import time
from threading import Lock
from queue import Queue

i = 0


def Producer(num: int, _q: Queue, _producer_lock: Lock):
    global i
    print(f"{num} 开始生产数据\n")
    while 1:
        if i > 100:
            break
        elif _q.qsize() == 0:
            _q.put(i)
            with _producer_lock:
                print(f"由生产者{num}生产的{i}进入队列\n")
                i += 1
        time.sleep(0.001)
