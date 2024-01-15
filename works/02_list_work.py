from datetime import datetime

# 1. 查找有没有满分10分或者0分，去掉最高分与最低分，输出结果
list = [8, 8.5, 9, 9.5, 8.2, 10, 6, 8.8, 9.2, 8.2]
list.sort()
# print(list) # [6, 8, 8.2, 8.2, 8.5, 8.8, 9, 9.2, 9.5, 10]
new_list = []
for num in list:
  if (num == 0 or num == 10 or num == list[0]):
    continue
  else:
    new_list.append(num)

print(list)
print(new_list) # [8, 8.2, 8.2, 8.5, 8.8, 9, 9.2, 9.5]

# 2. 编写程序 存储 3个番的信息，其中保存 番名、评分、发布时间
fan_list = [None] * 3
for index, value in enumerate(fan_list):
  print(value)
  fan_list[index] = {
    'name': f'fan{index + 1}',
    'rate': f'{index + 1}',
    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  }

print(fan_list)
'''
[
  {'name': 'fan1', 'rate': '1', 'time': '2024-01-16 07:11:26'},
  {'name': 'fan2', 'rate': '2', 'time': '2024-01-16 07:11:26'},
  {'name': 'fan3', 'rate': '3', 'time': '2024-01-16 07:11:26'}
]
'''