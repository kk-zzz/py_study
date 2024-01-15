temp = '爱你一百遍 '*100
print(temp)
print('\n'.join(temp.split()))

print('to be or not to be'[::-1]) # eb ot ton ro eb ot

china = 'chinachinachina'
for char in china:
  if (char == 'c'):
    print(char)
  else:
    print(f'char: {char}')