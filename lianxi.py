import random
import time
import calendar
import os

#time 时间模块
'''
l = time.localtime(time.time())
print(l)
print(l[0],"年")
a = time.asctime(l)
print(a)
print(time.strftime(a))


'''
#calendar 日历模块
'''
l = calendar.month(2000,10)
print(l)
'''
'''
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)

ask_ok("qinss:")
'''
#把时间格式改为时间戳
# a = "Mon Oct 26 00:15:12 2020" 
# print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))


#获取当前时间的格式
# i = time.localtime(time.time())
# print(time.asctime(i))


while True:
    i = time.time()
    m = (1604999999.0)
    while True:      
        time.sleep(1)
        d = (m-i)
        h = d/60/60
        f = d/60
        s = d%60
        print("距离你还有%d:%d:%d"%(h,f,m))
        break
    if i >= m:
        print("你好")
        break

    

    





