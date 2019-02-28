import pandas as pd
from pandas import Series
fandango = pd.read_csv("fandango_score_comparison.csv")
series_film = fandango['FILM']
print(type(series_film))
print(series_film[0:5])
print('--------------------')
film_names = series_film.values
print(type(film_names))
print('--------------------')
series_rt = fandango['RottenTomatoes']
print(series_rt[:5])
rt_scores = series_rt.values
# print(rt_scores)
print('--------------------')
series_custom = Series(rt_scores, index=film_names)
print(series_custom)

