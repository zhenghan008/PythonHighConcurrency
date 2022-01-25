import time


def Consumer(num: int, q, consumer_lock):
    print(f"{num} 开始消费数据\n")
    while 1:
        if q.qsize() != 0:
            body = q.get()
            with consumer_lock:
                print(f"由消费者{num}消费的{body}出队列\n")
            time.sleep(0.001)
