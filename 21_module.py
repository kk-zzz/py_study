'''
模块使用的目的是：把别人写好的code引入到我们的文件中，可以直接使用别人封装好的method 或 class等

python使用模块有两种方式：
- import xxx
- from xxx import aa
'''

# import
import random
'''
1. randint 生成start到end之间的数字，包括 end值
'''
print(random.randint(0,100))

# form xx import aa
from random import randint
print(f'from-import: {randint(0,9)}')

'''
math 数学模块
'''
import math
print(math.ceil(3.1415726)) # 4
print(math.sqrt(4)) # 2.0
print(type(math.sqrt(4))) # <class 'float'>

'''
time 时间模块
'''
import time
print(time.time()) # 1705755425.4164102 当前时间戳
time.sleep(2) # sleep(sec) 程序睡眠 2s 再继续执行code
print(f'Hello, sleep 2s, current time: {time.time()}')

print(time.strftime('%Y-%m-%d %H:%M:%S')) # 1705755425.4164102 当前时间戳
time.sleep(2) # sleep(sec) 程序睡眠 2s 再继续执行code
print(f'Hello, sleep 2s, current time: {time.strftime('%Y-%m-%d %H:%M:%S')}')

from datetime import datetime
current_time = datetime.now()
print(f'格式化当前时间：{current_time.strftime('%Y-%m-%d %H:%M:%S') + '.{:06d}'.format(current_time.microsecond)}') # 格式化当前时间：2024-01-20 21:09:10.663418