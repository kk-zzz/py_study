def getDefault():
  return

print(f'getDefault Value: {getDefault()}') # getDefault Value: None


def getSum(a = 0, b = 0):
  rs = a + b
  return rs

print(getSum(1, 2)) # 3

def getParams(*args):
  for i in args:
    print(f'getParams args: {i}')
  # return args # tuple 类型 (1, 2, 3, ['a', 'b'])
print(f'getParams: {getParams(1, 2, 3, ['a', 'b'])}')
'''
getParams args: 1
getParams args: 2
getParams args: 3
getParams args: ['a', 'b']
getParams: None # 多打印一个默认的返回值 None
'''

def fun5(**k):
  print(f'k: {k}')
  print(f'k type: {type(k)}')
  for i in k:
    print(f'item in k: {i} -- {k.get(i)}')
  print(f'...: {k.get('gender')}')
  # print(f'...: {k['work']}') # 获取没有给定的 key名会报错
fun5() # {} # k type: <class 'dict'>
fun5(name = 'Apple', age = 18)
'''
k: {'name': 'Apple', 'age': 18}
k type: <class 'dict'>
item in k: name -- Apple
item in k: age -- 18
...: None
'''

# 约定参数类型
def fun6(a:int = 0, b:int = 0):
  print(a+b)
fun6() # 0
fun6(3, 7) # 10
# fun6(3, '7') # TypeError: unsupported operand type(s) for +: 'int' and 'str'


