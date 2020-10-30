from multiprocessing import Process
from threading import Thread
import os, random
from datetime import *
from time import sleep


def task():
    # t=Thread(target=time.sleep,args=(3,))
    # t.start()
    while True:
        print(datetime.now())
        print('%s is running' % os.getpid())
        sleep(2)
        print('%s is done' % os.getpid())


def thread_test():
    threads=[]
    for i in range(10):
        t = Thread(target=task)
        t.daemon = True
        threads.append(t)
    for i in threads:
        i.start()


if __name__ == '__main__':
    thread_test()
    print('主')
