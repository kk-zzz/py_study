# 1. 产生100以内的随机数，直到随机数为 66 时终止循环
from random import randint
while True:
  rs = randint(0, 100)
  if rs == 66:
    print(f'随机数字{rs}')
    break
  else:
    print(f'continue: {rs}')

# 2. 把100 ~ 200之间不能被 6 整除的数输出，并且每行输出10个
list = []
count = 0
for item in range(100, 201):
  if item % 6 == 0:
    list.append(item)
    continue
print(f'100～200之间能被6整除的数有：{list}')

for i in range(0, len(list), 10):
  print(list[i:i + 10]) # 截取