import threading
from datetime import datetime
import time

exec_count=0


def heart_beat(time_cycle):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    global exec_count
    exec_count += 1
    # 15秒后停止定时器
    if exec_count < time_cycle:
        threading.Timer(1, heart_beat,args=(time_cycle,)).start()


'''
cancel_tmr = False
def heart_beat1():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))

    if not cancel_tmr:
        threading.Timer(1, heart_beat1()).start()


heart_beat1()

# 15秒后停止定时器
time.sleep(15)
cancel_tmr = True
'''

if __name__ == "__main__":
    heart_beat(15)
