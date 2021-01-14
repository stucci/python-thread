# [Pythonで学ぶ 基礎からのプログラミング入門(33) マルチスレッド処理を理解しよう(後編) | マイナビニュース](https://news.mynavi.jp/article/python-33/)

import time, threading

# Class definition

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(10):
            print('MyThread: ' + str(i))
            time.sleep(1)

# Run threads

# mt = MyThread()  # create thread instance
# mt.start()  # start the thread
# for i in range(10):
#     print('Main: ' + str(i))
#     time.sleep(1)

class MyThread2(threading.Thread):
    def __init__(self, name, sleep_time):
        threading.Thread.__init__(self)
        self.name = name
        self.sleep_time = sleep_time

    def run(self):
        for i in range(10):
            print(self.name + ': ' + str(i))
            time.sleep(self.sleep_time)

# thread1 = MyThread2('A', 1)
# thread2 = MyThread2('B', 1)
# thread1.start()
# thread2.start()

class MyThread3(threading.Thread):
    def __init__(self, count):
        threading.Thread.__init__(self)
        self.count = count
        self.return_value = None   # RETURN VALUE

    def run(self):
        sum_value = 0
        for i in range(1, 1 + self.count):
            sum_value += i
            time.sleep(0.1)
        self.return_value = sum_value   # SET RETURN VALUE

    def get_value(self):  # GETTER METHOD
        return self.return_value

# thread1 = MyThread3(4)
# thread1.start()
# thread1.join()
# print(thread1.return_value)  # 15
# print(thread1.get_value())   # 15

global_counter = 5

class MyThread4(threading.Thread):
    def __init__(self, name, sleep_time):
        threading.Thread.__init__(self)
        self.name = name
        self.sleep_time = sleep_time

    def run(self):
        global global_counter

        # read
        count = global_counter
        print(self.name + ': read global_value ' + str(global_counter))

        # do something
        print(self.name + ': do something')
        time.sleep(self.sleep_time)

        # write
        global_counter = count - 1
        print(self.name + ': write global_value ' + str(global_counter))


# thread1 = MyThread4('A', 5)
# thread2 = MyThread4('B', 3)
# thread1.start()
# time.sleep(1)
# thread2.start()
# thread1.join()
# thread2.join()
# print('Result: ' + str(global_counter))

global_counter = 5
global_lock = threading.Lock()   # LOCK OBJECT

class MyThread5(threading.Thread):
    def __init__(self, name, sleep_time):
        threading.Thread.__init__(self)
        self.name = name
        self.sleep_time = sleep_time

    def run(self):
        global global_counter
        global global_lock

        # LOCK
        global_lock.acquire()

        count = global_counter
        print(self.name + ': read global_value ' + str(global_counter))
        print(self.name + ': do something')
        time.sleep(self.sleep_time)
        global_counter = count - 1
        print(self.name + ': write global_value ' + str(global_counter))

        # RELEASE
        global_lock.release()

# thread1 = MyThread5('A', 5)
# thread2 = MyThread5('B', 3)
# thread1.start()
# time.sleep(1)
# thread2.start()
# thread1.join()
# thread2.join()
# print('Result: ' + str(global_counter))

global_counter = 5
global_semaphore = threading.Semaphore(1)   # SEMAPHORE OBJECT

class MyThread6(threading.Thread):
    def __init__(self, name, sleep_time):
        threading.Thread.__init__(self)
        self.name = name
        self.sleep_time = sleep_time

    def run(self):
        global global_counter
        global global_lock

        # LOCK
        global_semaphore.acquire()

        count = global_counter
        print(self.name + ': read global_value ' + str(global_counter))
        print(self.name + ': do something')
        time.sleep(self.sleep_time)
        global_counter = count - 1
        print(self.name + ': write global_value ' + str(global_counter))

        # RELEASE
        global_semaphore.release()

thread1 = MyThread6('A', 5)
thread2 = MyThread6('B', 3)
thread1.start()
time.sleep(1)
thread2.start()
thread1.join()
thread2.join()
print('Result: ' + str(global_counter))
