# [Pythonで学ぶ 基礎からのプログラミング入門(32) マルチスレッド処理を理解しよう(前編) | マイナビニュース](https://news.mynavi.jp/article/python-32/)

import time, urllib.request, urllib.error, threading

# time_before = time.time()
# time.sleep(5)
# time_after = time.time()
# time_elapsed = time_after - time_before
# print(time_elapsed)
# # ### -> 5.009

# sum_value = 0
# current_time = time.time()
# for i in range(0, 100000):
#     None
# print(time.time() - current_time)
# ### -> 0.004

# sum_value = 0
# current_time = time.time()
# for i in range(0, 100000):
#     sum_value += i
# print(time.time() - current_time)
# ### -> 0.015

# sum_value = 0
# current_time = time.time()
# for i in range(0, 10000):
#     sum_value += i
#     print(sum_value)
# print(time.time() - current_time)
# ### -> 5.090

# sum_value = 0
# current_time = time.time()
# f = open('./a.txt', 'a')
# for i in range(0, 10000):
#     sum_value += i
#     f.write(str(sum_value) + '\n')
# f.close()
# print(time.time() - current_time)
# ### -> 0.027

current_time = time.time()
urls = ['http://www.google.com', 'http://www.yahoo.co.jp/', 'https://www.bing.com/']
for url in urls:
    response = urllib.request.urlopen(url)
    html = response.read()
print(time.time() - current_time)
### -> 0.789

def prints(name, sleep_time):
    for i in range(10):
        print(name + ': ' + str(i))
        time.sleep(sleep_time)

thread1 = threading.Thread(target=prints, args=('A', 1,))  # Initialize
thread2 = threading.Thread(target=prints, args=('B', 1,))

"""multi thread"""
# thread1.start() # Start
# thread2.start()

"""single thread"""
# prints('A', 1)
# prints('B', 1)

"""multi thread (wait)"""
# thread1.start()
# thread1.join()  # WAIT HERE
# thread2.start()

def get_html(url):
    current_time = time.time()
    response = urllib.request.urlopen(url)
    html = response.read()
    print(url + ': ' + str(time.time() - current_time))

urls = ['http://www.google.com', 'http://www.yahoo.co.jp/', 'https://www.bing.com/']
threads = []

# Start Threads
current_time = time.time()
for url in urls:
    thread = threading.Thread(target=get_html, args=(url,))
    thread.start()
    threads.append(thread)

# Wait Threads
for thread in threads:
    thread.join()

print('Time: ' + str(time.time() - current_time))
### -> 0.272 (about 3 times than single thread)
