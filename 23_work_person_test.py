'''
1. 创建person模块，在模块中创建 student 类，包含属性name、age和 self_intro方法
'''
# person modules is in createModules

'''
2. 创建 person_test.py 文件调用person中的类，创建对象 student，调用self_intro 方法
'''
from createModules import person
s1 = person.Student('Cherry', 16)
print(s1.self_intro('reading'))

