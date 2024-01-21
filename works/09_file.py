'''
1. 创建 text.txt 并输入 100行192.168.1.0-50的IP地址，例如：
192.168.1.1 192.168.1.2 192.168.1.32
'''

from random import randint

f = open('text.txt', 'w')
for i in range(100):
  break_op = '\n' if i != 100 else ''
  f.write(f'192.168.1.{randint(0, 50)}{break_op}')
f.close()


'''
2. 统计text.txt 文件中 192.168.1.6 的 IP出现的频率
'''
count = 0
f1 = open('text.txt', 'r')
rs = f1.readlines()

for i in rs:
  count = count + 1 if '192.168.1.6' in i else count

print(f'192.168.1.6 出现的次数是：{count}')
f1.close()
