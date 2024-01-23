def sorted_by_key(lst, sort_key, reverse):
  """
  Sort a list of dictionaries by a specified key.

  Parameters:
  lst (list): List of dictionaries.
  sort_key (str): Key in the dictionary to sort by.
  reverse (bool): Whether to sort in descending order.

  Returns:
  list: Sorted list.
  """
  return sorted(lst, key=lambda x: x[sort_key], reverse=reverse)

if __name__ == '__main__':
  # 测试函数
  movie_list = [
      {'title': 'Whispers of the Past', 'rating': 8.0, 'date': '2018-07-07'},
      {'title': 'Under the Moonlight', 'rating': 7.5, 'date': '2018-05-21'},
      {'title': 'A Night in Paris', 'rating': 7.6, 'date': '2018-12-14'}
  ]
  # 使用函数按日期排序
  import json
  sorted_movies_by_date = sorted_by_key(movie_list, 'date', True)  # Sort by date in descending order
  print(f'sorted_movies_by_date_json: {json.dumps(sorted_movies_by_date, indent=2)}')
  '''
  sorted_movies_by_date_json: [
    {
      "title": "A Night in Paris",
      "rating": 7.6,
      "date": "2018-12-14"
    },
    {
      "title": "Whispers of the Past",
      "rating": 8.0,
      "date": "2018-07-07"
    },
    {
      "title": "Under the Moonlight",
      "rating": 7.5,
      "date": "2018-05-21"
    }
  ]
  '''

  print()
  print('='*10)
  print()

  # 测试函数
  movie_list2 = [
    ['Whispers of the Past', 8.0, '2018-07-07'],
    ['Under the Moonlight', 7.5, '2018-05-21'],
    ['A Night in Paris', 7.6, '2018-12-14']
  ]
  sorted_movies_by_index = sorted_by_key(movie_list2, 2, True)  # Sort by date in descending order
  print(f'sorted_movies_by_index_json: {json.dumps(sorted_movies_by_index, indent=2)}')
  '''
  sorted_movies_by_index_json: [
    [
      "A Night in Paris",
      7.6,
      "2018-12-14"
    ],
    [
      "Whispers of the Past",
      8.0,
      "2018-07-07"
    ],
    [
      "Under the Moonlight",
      7.5,
      "2018-05-21"
    ]
  ]
  '''
else:
  print('list_sorted')
