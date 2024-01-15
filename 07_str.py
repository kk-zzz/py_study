name1 = 'KK'
name2 = 'Apple'

print(name1)
print(name2)
print(type(name1)) # <class 'str'>
print(type(name2)) # <class 'str'>

# ''' 很像JS 中模板字符串 '''
info1 = '''
Hello World,
To Be Yourself
'''
print(info1)
print(type(info1)) # <class 'str'>

info2 = """
222 Hello World,
222 To Be Yourself
"""

print(info2)
print(type(info2)) # <class 'str'>

# \ 转义字符 与JS一样
say1 = 'I\'m KK'
print(say1)

say2 = "I'm Apple"
print(say2)
