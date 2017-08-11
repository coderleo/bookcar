#coding=utf-8
import book
import multiprocessing
from config import WORKER
if __name__ == '__main__':
    for i in range(WORKER):
        p = multiprocessing.Process(target=book.start, args=(i,))
        p.start()

