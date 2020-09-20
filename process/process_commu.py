#!-*- coding:utf-8 -*-
'''from multiprocessing import Process,Queue
import os,time,random

def write(q):
	print('Process to write %s'% os.getpid())
	for value in ['A','B','C']:
		print('put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	print('Process to read %s' %os.getpid())
	while True:
		value=q.get(True)
		print('Get %s from quene.' % value)
		
if __name__=='__main__':
	q=Queue()
	pw=Process(target=write,args=(q,))
	pr=Process(target=read,args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()'''
	
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
    #print(type(res))
    print(res.get())
  print("Sub-process(es) done.")



