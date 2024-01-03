from multiprocessing import Process
import os


def fnc():
    print(os.getpid(), os.getppid())


if __name__ == "__main__":
    print("main:", "\t", os.getpid(), os.getppid())
    p = Process(target=fnc)
    # 注意这里如果传入fnc()将无法开启新的进程
    # 注意这里的fnc作为参数传入不能加括号，否则无法成功开启新的进程。
    p.start()
    p.join() # 等待p进程结束，再执行后面的代码