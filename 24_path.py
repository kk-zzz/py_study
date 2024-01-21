'''
路径的操作
  - 相对路径
  - 绝对路径
'''

# 相对路径
# 绝对路径

import os
print(os.getcwd()) # /Users/f2e/KK_Study/py_code 返回当前根目录的绝对路径
print(os.path.abspath('createModules')) # /Users/f2e/KK_Study/py_code/createModules 返回指定文件的绝对路径
print(os.path.dirname('24_path.py')) # 啥也没有
print(os.path.dirname('/Users/f2e/KK_Study/py_code/createModules')) # /Users/f2e/KK_Study/py_code 参数需要给绝对路径
print(os.path.dirname(r'/createModules/person.py')) # 获取上一层文件夹的位置 /createModules 参数可以是 r'相对路径'

# exists 判断文件夹或文件是否存在
print(os.path.exists('/Users/f2e/KK_Study/py_code')) # True
print(os.path.exists('/Users/f2e/KK_Study/aaa')) # False
print(os.path.exists('/Users/f2e/KK_Study/py_code/24_path.py')) # True
print(os.path.exists('/Users/f2e/KK_Study/py_code/24_path_test.py')) # False

# split 分割 Return tuple(head, tail)把最后一个文件或文件夹名 单独抽离出来
print(os.path.split('/Users/f2e/KK_Study/py_code')) # ('/Users/f2e/KK_Study', 'py_code')
print(os.path.split('/Users/f2e/KK_Study/py_code/24_path.py')) # ('/Users/f2e/KK_Study/py_code', '24_path.py')

# splitext 判断最后一个文件或文件夹名的 后缀是什么
print(os.path.splitext('/Users/f2e/KK_Study/py_code')) # ('/Users/f2e/KK_Study/py_code', '')
print(os.path.splitext('/Users/f2e/KK_Study/py_code/24_path.py')) # ('/Users/f2e/KK_Study/py_code/24_path', '.py')


# isFile 判断是不是一个文件
print(os.path.isfile('/Users/f2e/KK_Study/py_code')) # False
print(os.path.isfile('/Users/f2e/KK_Study/py_code/24_path.py')) # True
print(os.path.isfile(r'24_path.py')) # True

# isdir 判断是不是一个文件夹
print(os.path.isdir('/Users/f2e/KK_Study/py_code')) # True
print(os.path.isdir('/Users/f2e/KK_Study/py_code/24_path.py')) # False

# 展示当前文件
print(os.listdir())
'''
['19_function.py', '10_str_subscript.py', '14_if.py', '12_list.py', '.DS_Store', '18_break_continue.py', '06_logical_operator.py', '01_code.py', '23_third_module_pip.py', '05_compare_operator.py', '15_multi_if.py', '02_variables.py', '03_data_type.py', '17_while.py', '07_str.py', 'works', '22_invoke_module1.py', 'createModules', '04_assignment_operator.py', '08_input.py', '16_trinomial_operator.py', '.git', '21_module.py', '09_format.py', '11_str_methods.py', '23_work_person_test.py', '24_path.py', '20_class.py', '13_dict.py']
'''

print(os.listdir('./works'))
'''
['02_list_work.py', '07_class.py', '.DS_Store', '08_use_person_by_me.py', '__init__.py', '01_str_work.py', '06_function.py', '__pycache__', '04_while.py', '03_if_work.py', '05_break.py']
'''