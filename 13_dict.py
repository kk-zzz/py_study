dict1 = {}
dict2 = dict()
dict3 = {'name': '涂山红红', 'from': '狐妖小红娘', 'date': '2015-06-26'}
print(dict1) # {}
print(dict2) # {}
print(dict3) # {'name': '涂山红红', 'from': '狐妖小红娘', 'date': '2015-06-26'}
print(type(dict1)) # <class 'dict'>
print(type(dict2)) # <class 'dict'>
print(type(dict3)) # <class 'dict'>

# 若是没有 name 即增加此 key-value，否则是修改 name 的 value
dict1['name'] = 'KK'
print(dict1) # {'name': 'KK'}
dict1['name'] = 'Cherry'
print(dict1) # {'name': 'Cherry'}

# 推荐使用  get 获取数据
print(dict1.get('name')) # Cherry
print(dict1['name']) # Cherry
print(dict1.get('age')) # None
# print(dict1['age']) # KeyError: 'age'

# 获取所有的 keys
print(dict3.keys()) # dict_keys(['name', 'from', 'date'])
# 获取所有的 values
print(dict3.values()) # dict_values(['涂山红红', '狐妖小红娘', '2015-06-26'])
# 获取所有的 key-value
print(dict3.items()) # dict_items([('name', '涂山红红'), ('from', '狐妖小红娘'), ('date', '2015-06-26')])

# del 删除数据
del dict1['name']
print(dict1) # {}

# clear 清空dict = {}
dict3.clear()
print(dict3) # {}
