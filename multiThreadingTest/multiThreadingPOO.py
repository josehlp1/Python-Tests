import threading
import time

class Tasks:
    def thread_delay(thread_name, delay):
        count = 0
        while count < 3:
            time.sleep(delay)
            count += 1
            print(thread_name, '-------->', time.time())

task = Tasks

t1 = threading.Thread(target=task.thread_delay('thread_1', 0), args=('t1', 1))
t2 = threading.Thread(target=task.thread_delay('thread_2', 0), args=('t2', 1))
t1.start()
t1.join()
t2.start()
print('Threading finish!')