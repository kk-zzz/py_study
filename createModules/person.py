class Student:
  def __init__(self, name:str, age:int) -> None:
    self.name = name
    self.age = age

  def self_intro(self, hobby:str):
    return f'Hello Everyone, my name is {self.name}, I\'m {self.age}, and I like {hobby}'
  
if __name__ == '__main__':
  s1 = Student('Apple', 18)
  print(s1.self_intro('hiking')) # Hello Everyone, my name is Apple, I'm 18, and I like hiking