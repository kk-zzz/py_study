'''
使用第三方模块：

pip3 install
pip3 list
pip3 uninstall
'''

# matplotlib 创建图表图形
'''
pip3 install matplotlib
'''
# as plt 是 pyplot 的别名是 plt
from matplotlib import pyplot as plt

# 1. 数据
x = [1, 2, 3]
y = [55, 89, 90]

# 2. 创建图表
plt.plot(x, y)

# 3. 添加标题和标签
plt.title('Simple Plot')
plt.xlabel('xAixs')
plt.ylabel('yAixs')

# 4. 显示图表
plt.show()
