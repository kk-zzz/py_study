'''
1. 定义个函数实现：计算年龄并返回的功能
比如：输入出生年2000，今年份2050，函数返回50的结果
提示：记得用数据类型转换 int(num)
'''
# def getAge():
#   born = input('请输入你的出生公历年份：')
#   today = input('请输入今年公历年份：')
#   age = int(today) - int(born)
#   print(f'您的年龄是：{age}')
# getAge()

'''
2. 定义一个函数实现：查找数据容器中是否存在评分超过9.5分的番剧并返回超过9.5分的番剧信息
'''
# def getserialInfo(*args): # 只能取 args[0]
def getserialInfo(args):
  for i in args:
    # if i['rate'] >= 9.5: # ok
    if i.get('rate') >= 9.5: # ok
      print(f'i: {i}')

from random import randint
getserialInfo(
  [
    { 'name': 'Apple', 'rate': randint(3, 10) },
    { 'name': 'Cherry', 'rate': randint(3, 10) },
    { 'name': 'Harry', 'rate': 9.8 },
    { 'name': 'KK', 'rate': randint(3, 10) },
  ]
)