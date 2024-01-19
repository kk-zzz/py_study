# 查找、判断、修改
info = 'Hello python and KK and world, to be yourself'

# find index count
print(info.find('KK')) # 17
print(info.find('KK', 0, 5)) # -1 找不到就是 -1
print(info.find('KK', 15, 20)) # 17

print(info.index('and')) # 13
print(info.index('and', 18)) # 20
# print(info.index('ands')) # 没有找到就报错 ValueError: substring not found

print(info.count('be')) # 1
print(info.count('be', 10, 20)) # 0 找不到就是 0
print(info.count('bes')) # 0

print(info.count('and')) # 2

'''
修改
'''
print(info) # Hello python and KK and world, to be yourself
# 全大写
print(info.upper()) # HELLO PYTHON AND KK AND WORLD, TO BE YOURSELF
# 全小写
print(info.lower()) # hello python and kk and world, to be yourself
# 所有单词的 第一个字母大写
print(info.title()) # Hello Python And Kk And World, To Be Yourself
# 只有第一个单词的第一个字母大写
print(info.capitalize()) # Hello python and kk and world, to be yourself


'''
替换
'''
print(info.replace('and', '和')) # Hello python 和 KK 和 world, to be yourself
print(info) # Hello python and KK and world, to be yourself
print(info.replace('and', 'add', 1)) # Hello python add KK and world, to be yourself

'''
分割 & 拼接
'''
print(info.split()) # ['Hello', 'python', 'and', 'KK', 'and', 'world,', 'to', 'be', 'yourself']
print(info.split('and')) # ['Hello python ', ' KK ', ' world, to be yourself']

# 拼接
tmp = info.split()
print(','.join(tmp)) # Hello,python,and,KK,and,world,,to,be,yourself
print('\n'.join(tmp))
'''
Hello
python
and
KK
and
world,
to
be
yourself
'''

'''
去除空格
'''
info2 = '     Hahaha, I love apple    '
print(info2.strip()) # Hahaha, I love apple
print(info2.lstrip()) # Hahaha, I love apple    
print(info2.rstrip()) #      Hahaha, I love apple


# starhtswith endswth 判断是否是指定的字符 bool
print(info.startswith('Hello')) # True
print(info.startswith('hello')) # False
print(info.endswith('self')) # True
print(info.endswith('kk')) # False

# 判断是否是纯数字
print('123'.isdigit()) # True
# 判断是否是纯字母
print('abc'.isalpha()) # True
# 判断是否是字母+数字
print('abc123'.isalnum()) # True
print('abc_'.isalnum()) # False

# encode & decode
name = '张张'
encode_name = name.encode()
print(f'encode {name}: {encode_name}') # encode 张张: b'\xe5\xbc\xa0\xe5\xbc\xa0'
print(f'{name} length: {len(name)}') # 张张 length: 2


