"""
buy ticket script to introduce Lock class
"""

from multiprocessing import Process, Lock
import json
import os


def search(i):
    with open("tickets_count", encoding="utf-8") as f:
        ticket = json.load(f)
    print(f"{i}:num of tickets remaining is {ticket['count']}.")
    # print(f"{i}:num of tickets remaining is {ticket}.")
    # print("%s:num of tickets remaining is %s" % (i, ticket["count"]))


def buy_ticket(i):
    with open("tickets_count", encoding="utf-8") as f:
        ticket = json.load(f)
    if ticket["count"] > 0:
        ticket["count"] -= 1
        print(f"{i} got the ticket.")
        # print("%s got the ticket." % i)
    with open("tickets_count", mode="w", encoding="utf-8") as f:
        json.dump(ticket, f)


def get_ticket(i, lock):
    search(i)
    with lock:# 给买票的操作加锁
        buy_ticket(i)


if __name__ == "__main__":
    lock = Lock()
    for i in range(10):
        Process(target=get_ticket, args=(i, lock)).start()