import threading
import time
import os
import requests
from urllib3.connectionpool import xrange
 
 
def get_document(url):
    # print(url)
    try:
        get = requests.get(url)
        data = get.content
        get.close()
    except:
        time.sleep(3)
        try:
            get = requests.get(url)
            data = get.content
            get.close()
        except:
            time.sleep(3)
            get = requests.get(url)
            data = get.content
            get.close()
    return data
 
 
def download_img(start, count):
    for i in xrange(start, count):
        src = "https://lns.hywly.com/a/1/" + str(i) + "/"
        for j in xrange(50):
            document = get_document(src + str(j) + '.jpg')
            if str(document).find("404 Not Found") > 0:
                break
            path = 'd:/SanMu/image/' + str(i) + '/'
            if not os.path.exists(path):
                os.makedirs(path)
            open(path + str(j) + '.jpg', 'wb').write(document)
 
 
thread_list = []
for i in xrange(0, 6):#想要几个线程就把3改成几
    thread = threading.Thread(target=download_img, args=(i * 1000, (i + 1) * 1000))
    thread_list.append(thread)
for thread in thread_list:
    thread.start()
for thread in thread_list:
    thread.join()
while 1:
    break