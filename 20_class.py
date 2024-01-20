class Person:
  def __init__(self, name:str, sex:str='male', hobby:str='抽烟，喝酒，烫头') -> None:
    self.name = name
    self.sex = sex
    self.hobby = hobby

  def eat(self):
    print('干饭了，干饭了')

  def study(self, info:str):
    print(f'Good Good Study, Day Day Up ~~ {info}')

  def self_intro(self) -> str:
    return f'我是{self.name}, 我的爱好是{self.hobby}'

p1 = Person('Apple')
print(p1.hobby) # 抽烟，喝酒，烫头
p1.eat() # 干饭了，干饭了
p1.study('python') # Good Good Study, Day Day Up ~~ python
print(p1.self_intro()) # 我是Apple, 我的爱好是抽烟，喝酒，烫头

