import threading


localschool=threading.local()
#创建全局threading.local对象


def process_student():
    #获取当前线程关联的student
    std = localschool.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
    #	threading.current_thread() 返回调用者当前的 Thread 对象


def process_thread(name):
    localschool.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='thread01')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
