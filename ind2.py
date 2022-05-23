#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Для своего индивидуального задания лабораторной работы 2.23 необходимо
организировать конфейер, в которм сначала в отдельном потоке вычисляется
значение первой функции, после чего результаты вычисления должны передаваться
второй функции, вычисляемой в отдельном потоке. Потоки для вычисления значений
двух функций должны запускаться одновременно
"""

from threading import Thread, Lock
from queue import Queue
from math import exp, factorial

accuracy = 0.0000001

Queue = Queue()
Lock = Lock()


def sum1(x=2):
    Lock.acquire()
    s, n, cur = 0, 1, 0
    while True:
        pre = (x ** (n + 2)) / factorial(n + 2)
        n += 2
        if abs(cur - pre) < accuracy:
            break
        cur = (x ** (n + 2)) / factorial(n + 2)
        s += cur
    Queue.put(s)
    Lock.release()


def func_y(x):
    yx = (exp(x) - exp(-x)) / 2
    print(yx)


if __name__ == '__main__':
    th1 = Thread(target=sum1).start()
    th2 = Thread(target=func_y(Queue.get())).start()
