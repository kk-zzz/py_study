name = 'KK'
print(name)

# 以下写法需要保证左右两边 数量相等，不然报错
num1, num2, num3 = 10, 20, 30
print(num1) # 10
print(num2) # 20
print(num3) # 30

a = b = 100
print(a) # 100
print(b) # 100

'''
+= -= *= ...
'''
a += b
print(a) # 200

a -= b
print(a) # 100

a *= b
print(a) # 10000

a /= b
print(a) # 100.0

a %= b
print(a) # 0.0

a = 100
a //= b
print(a) # 1