import pandas as pd

tmdb = pd.read_csv("tmdb_5000_movies.csv")
print(tmdb)

print(tmdb.vote_average.unique()) # a funcao 'unique' permite a visualizacao de cada nota unica, o retorno é uma variavel de escala intervalar
