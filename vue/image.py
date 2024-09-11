from PIL import Image

# 创建一张宽375高64的空白图片
image = Image.new("RGB", (375, 64), "pink")
image_blue = Image.new("RGB", (375, 64), "skyblue")

# 保存图片
image.save("zongzi.png")
image_blue.save('sky-blue.png')

print("图片已生成并保存为 zongzi.png")