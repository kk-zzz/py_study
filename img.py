from PIL import Image
# 创建一个 200*200像素的纯白色图片
img = Image.new('RGB', (200, 200), color = 'white')
# save img
img.save('200*200.png')
print('图片已生成并保存为200*200.png')
