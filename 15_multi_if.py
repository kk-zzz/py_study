year = 2021
level = 4

if year > 2020:
  if level == 0:
    print('已点赞')
  elif level == 1:
    print('已点赞，已投币')
  elif level == 2:
    print('已点赞，已投币，已收藏')
  elif level == 3:
    print('已点赞，已投币，已收藏，已转发')
  else:
    print('白嫖党') # 白嫖党
else:
  print('洗洗睡吧')