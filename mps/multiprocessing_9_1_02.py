"""
another way to start process
"""

from multiprocessing import Process
import os
import time


class MyProcess(Process):
    def __init__(self, a, b, c):
        super().__init__() # 这里视为在执行父类的init方法，没有这一行可能会出现unexpected报错
        self.a = a
        self.b = b
        self.c = c

    def run(self) -> None:
        time.sleep(1)
        print(os.getpid(), os.getppid(), self.a, self.b, self.c)


if __name__ == "__main__":
    print("-->", os.getpid())
    for i in range(10):
        p = MyProcess(1, 2, 3)
        p.start()