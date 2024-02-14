import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Analizing movies
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

print(movies.head())
print(ratings.query("movieId==1").rating)# mostra as notas somente do filme 1, ao colocar . rating no final ele so mostra a nota se eu tiro ele coloca todas as infos do filme 1
meanR1 = (ratings.query("movieId==1").rating.mean())
print("Mean rating movie 1 = ", meanR1)
#PAREI NO MIN 4:45

# agrupar todas as notas pela coluna filmeId:
# ratings.groupby("movieID") -> aqui eu o retorno vai ser um objeto do tipo DataFrameGroupBy (um agrupamento de valores) do Pandas:
# ratings.groupby("movieID").mean().plot(kind="bar")
# print(ratings.groupby("movieId").mean()) # acabamos tirando a média também do usuarioId e do momento
mean_movie_rating = ratings.groupby("movieId").mean()["rating"]
print(mean_movie_rating.head())

mean_movie_rating.plot(kind="hist")
plt.show()

# sns.boxplot(mean_movie_rating)
plt.figure(figsize=(5,8))# serve para definir uma proporção para nosso boxplot, como 5x8
sns.boxplot(y=mean_movie_rating)# o boxplot costuma ser feito na vertical (eixo y)
plt.show()

print(mean_movie_rating.describe()) # Para auxiliar na análise do gráfico, pedi as medidas descritivas desses dados
sns.histplot(mean_movie_rating, kde=True)
plt.show()

sns.histplot(mean_movie_rating, kde=True, bins=10)# uso o arguemento bins para poder definir o número de separações
plt.show()

plt.hist(mean_movie_rating)
plt.title("Movie average histogram")
plt.show()
