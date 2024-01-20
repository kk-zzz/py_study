'''
1. 定义一个学生类，
  - 包含：id、name、score、age四个属性
  - 包含：study方法
'''

class Students:
  def __init__(self, id:int, name:str, score:int, age:int) -> None:
    self.id = id
    self.name = name
    self.score = score
    self.age = age

  def study(self, lesson:str) -> str:
    return f'{self.name}最喜欢学习 {lesson}'
    

'''
2. 调用创建好的学生类，创建两个学生对象：
  -1 id: 1001, name: Allen, score: 90, age:18
  -2 id: 1002, name: Cherry, score: 100, age:20
  -3 调用其中一个对象的 study方法
'''
s1 = Students(1001, 'Allen', 90, 18)
s2 = Students(1002, 'Cherry', 100, 20)

print(s1.study('English')) # Allen最喜欢学习 English
print(s2.study('Chinese')) # Cherry最喜欢学习 Chinese