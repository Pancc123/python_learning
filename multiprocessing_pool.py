#! -*- coding:utf-8 -*-
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
import multiprocessing
import time


def func(msg):
  for i in range(3):
    print(msg)
    time.sleep(1)
  return "done " + msg

if __name__ == "__main__":
  pool = multiprocessing.Pool(processes=4)
  result = []
  for i in range(10):
    msg = "hello %d" %(i)
    result.append(pool.apply_async(func, (msg, )))
  pool.close()
  pool.join()
  for res in result:
    print(res.get())
  print("Sub-process(es) done.")