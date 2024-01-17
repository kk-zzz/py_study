# print('好好学习，天天向上')

i = 0
while i < 5:
  print('好好学习，天天向上')
  i += 1
  if i == 5:
    print('end')

# 计算1-100之间的累加和
count = 0
sum = 0
while count <= 100:
  sum += count
  count += 1
print(f'1到100的累积和是: {sum}') # 5050

# for
for a in 'python':
  print(a)
'''
p
y
t
h
o
n
'''

for item in ['aa', 67, 'kk']:
  print(item)
'''
aa
67
kk
'''

# for 实现1-100累加和
rs = 0
for i in range(101):
  rs += i
print(f'for 实现1-100累加和: {rs}')

# 嵌套循环
infos = [
  ['初审小当家', '美少年', '大舞台'],
  ['老友记', '绝望主妇', '生活大爆炸'],
  ['时光音乐会', '少年行', '狐妖小红娘']
]

# define function 将 1、2、3 转成 一、二、三
def arabic_to_chinese(number):
  # 定义数字到中文的映射
  chinese_numbers = {
    '0': '零',
    '1': '一',
    '2': '二',
    '3': '三',
    '4': '四',
    '5': '五',
    '6': '六',
    '7': '七',
    '8': '八',
    '8': '九',
    '10': '十',
  }

  # 转换数字为字符串，然后替换每个数字为中文
  chinese_str = ''
  for digit in str(number):
    chinese_str += ''.join(chinese_numbers[digit])
  return chinese_str
  
print(arabic_to_chinese(1)) # 一
print(arabic_to_chinese(12)) # 一二
print(type(arabic_to_chinese(124567))) # <class 'str'>


for index, info in enumerate(infos):
  print(f'周{arabic_to_chinese(index + 1)}')
  for item in info:
    print(f'info-item: {item}')
