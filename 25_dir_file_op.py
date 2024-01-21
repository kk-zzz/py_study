import os
from time import sleep
# makedirs 创建文件夹
# os.makedirs('tmp')

# sleep(2) # 程序睡2s 再继续执行

# # rmdir 删除文件夹
# os.rmdir('tmp')

f = open('test.py', 'w') # write 等于覆盖
f.write('hello test\n')
f.write('abc\n')
f.write('123')
f.close()

# f = open('test.py', 'a') # add or append 等于追加内容
# f.write('hello test 1\n')
# f.write('abc 2\n')
# f.write('123 3\n')
# f.close()

# # 简化code，使用 with 就不用再考虑 close的问题
# with open('test.py', 'a') as f:
#   f.write('hello test 1\n')
#   f.write('abc 2\n')
  # f.write('123 3\n')

# read file
with open('test.py', 'r') as f:
  print(f.read()) # 读取指定字节的内容
  '''
  hello test
  abc
  123
  '''
  f.seek(0)  # 确保文件指针在开头
  print(f.read(5)) # hello
  f.seek(0)  # 确保文件指针在开头
  print(f.readline()) # 读取一行 hello test
  f.seek(0)  # 确保文件指针在开头
  print(f.readlines()) # 读取所有行 # ['hello test\n', 'abc\n', '123']