movies = [
  ["The Grand Adventure", 8.5, "2021-07-15"],
  ["Mystery of the Blue", 7.8, "2019-11-22"],
  ["Lost in the Wild", 8.2, "2020-03-05"],
  ["Rise of a Hero", 9.1, "2022-05-30"],
  ["A Night in Paris", 7.6, "2018-12-14"],
  ["The Last Stand", 8.9, "2021-09-10"],
  ["Beyond the Horizon", 7.4, "2019-06-18"],
  ["Escape from Reality", 8.3, "2020-01-20"],
  ["Dreams of Space", 7.9, "2023-04-12"],
  ["Shadows in the Dark", 8.6, "2021-10-31"],
  ["Whispers of the Past", 8.0, "2018-07-07"],
  ["Chase the Light", 9.3, "2022-08-23"],
  ["The Forgotten Valley", 7.7, "2019-04-17"],
  ["Echoes of Time", 8.4, "2020-02-29"],
  ["Island of Secrets", 8.8, "2021-11-19"],
  ["Under the Moonlight", 7.5, "2018-05-21"]
]

'''
1. 将movies 按照时间从近到远排序，如 2022、2021、2020、2019
'''
from datetime import datetime
movies_by_year = {}
for movie in movies:
  print(f'{movie[2]}')
  year_obj = datetime.strptime(movie[2], '%Y-%m-%d')
  print(f'{movie[2]}--{year_obj}')
  year = datetime.strftime(year_obj, '%Y')
  print(f'{movie[2]}--{year_obj}=={year}')

  if year not in movies_by_year:
    movies_by_year[year] = []
  movies_by_year[year].append(movie)
  # tmp = {
  #   'name': movie[0],
  #   'rate': movie[1],
  #   'time': movie[2]
  # }
  # movies_by_year[year].append(tmp)

print(f'movies_by_year: {movies_by_year}')

# 按照时间排序
print()
sorted_movies_by_year = sorted(movies_by_year.items(), reverse=True)
print(f'sorted_movies_by_year: {sorted_movies_by_year}')
print()
new_sorted_movies_by_year = {}
for [year, movies] in sorted_movies_by_year:
  print(f'{year}--{movies}')
  # 将movies 按照时间排序
  sorted_movies = sorted(movies, key=lambda x: x[2], reverse=True)
  # print(f'sorted_movies: {sorted_movies}')
  new_sorted_movies_by_year[year] = sorted_movies
print()

# 使用json 将其格式化一下
import json
new_sorted_movies_by_year_json = json.dumps(new_sorted_movies_by_year, indent=2)
print(f'new_sorted_movies_by_year_json--{new_sorted_movies_by_year_json}')

'''
{
  "2023": [
    [
      "Dreams of Space",
      7.9,
      "2023-04-12"
    ]
  ],
  "2022": [
    [
      "Chase the Light",
      9.3,
      "2022-08-23"
    ],
    [
      "Rise of a Hero",
      9.1,
      "2022-05-30"
    ]
  ],
  "2021": [
    [
      "Island of Secrets",
      8.8,
      "2021-11-19"
    ],
    [
      "Shadows in the Dark",
      8.6,
      "2021-10-31"
    ],
    [
      "The Last Stand",
      8.9,
      "2021-09-10"
    ],
    [
      "The Grand Adventure",
      8.5,
      "2021-07-15"
    ]
  ],
  "2020": [
    [
      "Lost in the Wild",
      8.2,
      "2020-03-05"
    ],
    [
      "Echoes of Time",
      8.4,
      "2020-02-29"
    ],
    [
      "Escape from Reality",
      8.3,
      "2020-01-20"
    ]
  ],
  "2019": [
    [
      "Mystery of the Blue",
      7.8,
      "2019-11-22"
    ],
    [
      "Beyond the Horizon",
      7.4,
      "2019-06-18"
    ],
    [
      "The Forgotten Valley",
      7.7,
      "2019-04-17"
    ]
  ],
  "2018": [
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
}
'''

print()
print('='*20)
print()
'''
2. 使用封装的方法进行排序
'''
from createModules import list_sorted
list_sorted.sorted_by_key(movies, 2, True)
# movie_list_by_list_sorted = list_sorted.sorted_by_key(movie, 2, True)
# import json
# movie_list_by_list_sorted_json = json.dumps(movie_list_by_list_sorted, indent=2)
# print(f'movie_list_by_list_sorted_json: {movie_list_by_list_sorted_json}')
