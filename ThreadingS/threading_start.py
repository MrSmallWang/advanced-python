"""
thread implementations
这里可以得到开启线程的耗时会远低于开启进程的耗时
"""

import time
from threading import Thread
# from multiprocessing import Process as Thread


def func(i):
    print(f"start{i}")
    time.sleep(1)
    print(f"end{i}")


if __name__ == '__main__':
    t_1 = []
    for i in range(10):
        t = Thread(target=func, args=(i, ))
        t.start()
        t_1.append(t)

    print("accomplishment-2")

    for t in t_1:
        t.join()

    print("accomplishment-1")