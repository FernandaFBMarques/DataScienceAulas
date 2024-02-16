import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tmdb = pd.read_csv("tmdb_5000_movies.csv")

# avaliacao de quantos idiomas existem no arquivo .csv

# contagem dos indices:
indexes = tmdb["original_language"].value_counts().index

# contagem dos valores:
values_ = tmdb["original_language"].value_counts().values

# contagem dos valores da coluna original_language
# transforma eles em dataframe
# reinicia os indice da coluna
language_count = tmdb["original_language"].value_counts().to_frame().reset_index()

# crio duas colunas: original_language e total
language_count.columns = ["original_language", "total"]
# imprimo os 5 primeiros elementos
print(language_count.head())

# PLOTAR com o SNS
# original language no eixo x
# total no eixo y e
# language_count como fonte dos dados
sns.barplot(x="original_language", y="total", data=language_count)
plt.show()

# GRAFICO DE BARRAS -> catplot()
# passo o argumento kind="count" para que seja feita a contagem dos elementos de cada categoria
sns.catplot(x="original_language", kind="count", data=tmdb)
plt.show()

#como podemos gerar um gráfico de pizza?
plt.pie(language_count["total"], labels=language_count["original_language"])
plt.show()
