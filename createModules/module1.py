def test1(a:int=0, b:int=0) -> int:
  return a+b

'''
if 判断的目的是是 在当前文件执行code，才会执行 print语句
'''
if __name__ == '__main__':
  print(test1(1, 2)) # 3