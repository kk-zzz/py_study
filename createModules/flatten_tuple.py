def flatten_tuple(tup):
  for item in tup:
    if isinstance(item, tuple):
      yield from flatten_tuple(item)
    else:
      yield item

if __name__ == '__main__':
  # 示例元祖
  nested_tumple = ((1, 2), (3, 4))
  # 展平元祖
  flat_tuple = tuple(flatten_tuple(nested_tumple))
  print(flat_tuple) # (1, 2, 3, 4)

  # 示例元祖
  nested_tumple = (("<Cell 'Sheet1'.A1>", "<Cell 'Sheet1'.B1>"), ("<Cell 'Sheet1'.A2>", "<Cell 'Sheet1'.B2>"))
  # 展平元祖
  flat_tuple = tuple(flatten_tuple(nested_tumple))
  print(flat_tuple) # ("<Cell 'Sheet1'.A1>", "<Cell 'Sheet1'.B1>", "<Cell 'Sheet1'.A2>", "<Cell 'Sheet1'.B2>")