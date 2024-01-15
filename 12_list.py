# ========== append ========== 
name_list = ['KK', 'Apple', 'Cherry']
print(name_list) # ['KK', 'Apple', 'Cherry']
name_list.append('Barry')
name_list.append('Demon')
print(name_list) # ['KK', 'Apple', 'Cherry', 'Barry', 'Demon']
name_list.append(['Harry', 'Leo' ])
print(name_list) # ['KK', 'Apple', 'Cherry', 'Barry', 'Demon', ['Harry', 'Leo']]

# ========== extend ========== 追加数据
name_list1 = ['KK', 'Apple', 'Cherry']
print(name_list1)
name_list1.extend(['Harry', 'Leo' ])
print(name_list1) # ['KK', 'Apple', 'Cherry', 'Harry', 'Leo']
name_list1.extend('abc')
print(name_list1) # ['KK', 'Apple', 'Cherry', 'Harry', 'Leo', 'a', 'b', 'c']

# ========== insert ========== 指定位置 追加数据
name_list2 = ['KK', 'Apple', 'Cherry']
name_list2.insert(0, 'Harry')
print(name_list2) # ['Harry', 'KK', 'Apple', 'Cherry']
name_list2.insert(3, 'Leo')
print(name_list2) # ['Harry', 'KK', 'Apple', 'Leo', 'Cherry']

# ========== del ========== 保留字 等于 JS 中 delete 可以直接删除对象的某个属性
name_list3 = ['KK', 'Apple', 'Cherry']
del name_list3[1]
print(name_list3) # ['KK', 'Cherry']

del name_list3
# print(name_list3) # name 'name_list3' is not defined

# ========== pop ========== 从尾巴 pop 等于 js array 的 pop, 但是JS-》Array 的pop不能传入参数
name_list4 = ['KK', 'Apple', 'Cherry']
name_list4.pop()
print(name_list4) # ['KK', 'Apple']
name_list4.pop(-2)
print(name_list4) # ['Apple']

# ========== remove ========== 参数是 value 而不是 index
name_list5 = ['KK', 'Apple', 'Cherry']
name_list5.remove('Apple')
print(name_list5) # ['KK', 'Cherry']

# ========== clear ==========
name_list6 = ['KK', 'Apple', 'Cherry']
name_list6.clear()
print(name_list6) # []

# ========== 修改 ========== 不能修改不存在的下标，也和JS中的Array不一样
name_list7 = ['KK', 'Apple', 'Cherry']
name_list7[1] = 'Leo'
print(name_list7) # ['KK', 'Leo', 'Cherry']
# name_list7[3] = 'Harry'
# print(name_list7) # list assignment index out of range


# ========== reverse ==========
name_list8 = ['KK', 'Apple', 'Cherry']
name_list8.reverse()
print(name_list8) # ['Cherry', 'Apple', 'KK']


# ========== sort ========== 默认从小到大排序, 与 JS 中 Array.sort 不一样
name_list9 = ['KK', 'Apple', 'Cherry']
name_list9.sort()
print(name_list9) #['Apple', 'Cherry', 'KK']

num = [56, 8, 89, 90, 4, 7]
num.sort()
print(num) # [4, 7, 8, 56, 89, 90]

# ========== in ==========
name_list10 = ['KK', 'Apple', 'Cherry']
print('KK' in name_list10) # True
print('Leo' in name_list10) # False

for word in name_list10:
  print(word)
'''
KK
Apple
Cherry
'''

