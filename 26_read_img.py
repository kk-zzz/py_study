# 图像、视频、音频：使用 'rb' 模式打开文件进行读取。其中 r 表示读取模式，b 表示二进制模式
with open('avatar.jpeg', 'rb') as f:
  print(f.read())

# 实现 img 的 copy
f1 = open('avatar.jpeg', 'rb')
f2 = open('avatar2.jpeg', 'wb')
f2.write(f1.read())

# 先确定写完，再关闭所读的文件
f2.close()
f1.close()