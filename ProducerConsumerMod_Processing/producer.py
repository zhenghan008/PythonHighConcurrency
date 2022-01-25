import time


i = 0


def Producer(num: int, q, producer_lock):
    global i
    print(f"{num} 开始生产数据\n")
    while 1:
        if i > 100:
            break
        elif q.qsize() == 0:
            q.put(i)
            with producer_lock:
                print(f"由生产者{num}生产的{i}进入队列\n")
                i += 1
        time.sleep(0.001)
