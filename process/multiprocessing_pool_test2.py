#! -*- coding:utf-8 -*-
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s (%s)...' % (name,(os.getpid())))
	start_time = time.time()
	time.sleep(random.random()*3)
	end_time = time.time()
	print('Task %s runs %0.2f seconds.' % (name,(end_time - start_time)))

	
if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p=Pool(4)
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print('Waitting for all subprocesses done...')
	p.close()
	p.join()
	print('ALL subprocesses done.')

# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。