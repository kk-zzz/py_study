# 1. 输入一个点的坐标（x,y），判断其所在的象限
x = input('请输入x坐标：')
y = input('请输入y坐标：')
if int(x) > 0 and int(y) > 0:
  rs = '第一象限'
elif int(x) < 0 and int(y) > 0:
  rs = '第二象限'
elif int(x) < 0 and int(y) < 0:
  rs = '第三象限'
elif int(x) > 0 and int(y) < 0:
  rs = '第四象限'
elif int(y) == 0 and int(x) != 0:
  rs = 'x轴上'
elif int(x) == 0 and int(y) != 0:
  rs = 'y轴上'
else:
  rs = '您在原点哦'
print(f'您属于的{int(x), int(y)}位于{rs}中')

'''
优化版本
'''
# 定一个function 处理 {x, y} 所在象限
def determine_quadrant(x, y):
    if x > 0 and y > 0:
      return '第一象限'
    elif x < 0 and y > 0:
      return '第二象限'
    elif x < 0 and y < 0:
      return '第三象限'
    elif x > 0 and y < 0:
      return '第四象限'
    elif x == 0 and y != 0:
      return 'y轴上'
    elif y == 0 and x != 0:
      return 'x轴上'
    else:
      return '您在原点哦'
    
def main():
    try:
      x = int(input('请输入x坐标：'))
      y = int(input('请输入y坐标：'))
      rs = determine_quadrant(x, y)
      print(f'坐标({x}, {y})位于{rs}中')
    except ValueError:
      print('请输入有效的数字。')

if __name__ == '__main__':
  main()

# 2. 输入一个分数，分数在0-100之间，90分以上是A，80到89是B，70到79是C，60到69是D，60以下是E

def rate_fun(value):
    if value >= 90:
      return 'A'
    elif value >=80:
      return 'B'
    elif value >= 70:
      return 'C'
    elif value >= 60:
      return 'D'
    else:
      return 'E'
    
def rate_main():
    try:
      value = int(input('请输入分数：'))
      rs2 = rate_fun(value)
      print(f'您的分数{value}，是{rs2}等级')
    except ValueError:
      print('请输入有效的数字。')

# 因为在直接运行的情况下，__name__ 总是等于 "__main__"
if __name__ == '__main__':
  rate_main()
