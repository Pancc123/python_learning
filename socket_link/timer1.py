# -*- coding: utf-8 -*-
import os, sys, time
import threading
import signal

TIMER = None


def timer_stop(signum, frame):
    global TIMER
    TIMER.cancel()


def timer_fun():
    global TIMER

    print("call timer fun")

    # 继续添加定时器，周期执行，否则只会执行一次
    TIMER = threading.Timer(2, timer_fun)
    TIMER.start()


if __name__ == "__main__":
    # 使用捕获信号结束定时器
    signal.signal(signal.SIGINT, timer_stop)

    # 参数：第一个是定时器时间间隔，第二个是定时器函数
    TIMER = threading.Timer(2, timer_fun)
    TIMER.start()

    time.sleep(30)