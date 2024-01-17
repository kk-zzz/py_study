'''
while 实现
'''
# 1. 计算1-100之间的累加和
count = 0
sum = 0
while count <= 100:
  sum += count
  count += 1
print(f'1到100的累积和是: {sum}') # 5050

# 2. 计算1-100 之间偶数的累加和
count = 0
sum = 0
while count <= 100:
  if count % 2 == 0:
    sum += count
  count += 1

print(f'1到100的偶数累积和是: {sum}') # 2550

# 2. 计算1-100 之间奇数的累加和
count = 0
sum = 0
while count <= 100:
  if count % 2 != 0:
    sum += count
  count += 1

print(f'1到100的奇数累积和是: {sum}') # 2500

'''
for 实现
'''
# 1. 计算1-100之间的累加和
sum = 0
for i in range(101):
  sum += i
print(f'for -> 1到100的累积和是: {sum}') # 5050

# 2. 计算1-100 之间偶数的累加和
sum = 0
for i in range(0, 101, 2):
  if i % 2 == 0:
    sum += i

print(f'for -> 1到100的偶数累积和是: {sum}') # 2550

# 2. 计算1-100 之间奇数的累加和
sum = 0
for i in range(1, 101, 2):
  if i % 2 != 0:
    sum += i

print(f'for -> 1到100的奇数累积和是: {sum}') # 2500

'''
打印
00000
11111
22222
33333
44444
'''
for i in range(5):
  print(str(i) * 5)
  