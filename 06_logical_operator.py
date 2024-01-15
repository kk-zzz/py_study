# and or not

a = 1
b = 2
c = 3

# and 只有两个都是True 才是 True，否则是 False
print(a > b and b > c) # False

# or 只要有一个是True，返回True，都是False则是 False
print(a > b or c > b) # True

# not 取反 非真即假 bool
# 比较运算符 优先级高于 逻辑运算符
print(not c > b) # False