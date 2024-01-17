# print('逛街买包')
# print('这个不错～～，买了，回家')
# print('这个不OK～～，再逛逛吧～～')

i = 1
while True:
  if i == 5:
    print('这个不错～～，买了，回家')
    break
  print('这个不OK～～，再逛逛吧～～')
  i += 1

'''
这个不OK～～，再逛逛吧～～
这个不OK～～，再逛逛吧～～
这个不OK～～，再逛逛吧～～
这个不OK～～，再逛逛吧～～
这个不错～～，买了，回家
'''

# for i in range(10):
#   print('点赞')
#   print('收藏')
#   print('投币')

from random import randint
print(randint(0, 3))
for i in range(10):
  num = randint(3, 10)
  print('='*10, f'第{ i + 1}部分 评分是：{num}', '='*10)
  if num < 8:
    print('点赞')
    continue
  if num < 9:
    print('收藏')
    continue
  if num < 10:
    print('投币')
    break


