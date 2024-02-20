import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tmdb = pd.read_csv("tmdb_5000_movies.csv")
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

ratings_toy_story = ratings.query("movieId==1")
ratings_jumanji = ratings.query("movieId==2")
print(len(ratings_toy_story), len(ratings_jumanji))
print("Toy Story's Average Rating: %.2f" % ratings_toy_story.rating.mean())
print("Jumanji's Average Rating: %.2f" % ratings_jumanji.rating.mean())

# Existe diferença entre essas médias, mas esse dado não consegue expressar, por exemplo,
# quantas pessoas amaram ou odiaram esses filmes, ou, em outros termos, quantas notas 5 ou 0,5 cada um desses filmes teve.

print("Toy Story's Median: %.2f" % ratings_toy_story.rating.median())
print("Jumanji's Median: %.2f" % ratings_jumanji.rating.median())
# estamos tentando resumir toda a distribuição dos dados em um único número,
# perdendo um volume muito grande de informação.

# Situacao hipotetica: 10 pessoas deram a nota 2.5 para um determinado filme
# Numpy eh capaz de fazer operações sobre esses conjuntos como a propria media
print(np.array([2.5] * 10).mean())

film1 = np.append(np.array([2.5] * 10), np.array([3.5] * 10)) # juncao de dois arrays para a variavel
film2 = np.append(np.array([5] * 10), np.array([1] * 10))

print(film1.mean(), film2.mean())
print(np.median(film1), np.median(film2))

# as duas tendências (a media e a mediana) trazem a mesma informação nesse conjunto de dados.
# Mas o comportamento dos dois filmes eh bem diferente.

# talvez seja melhor VISUALIZAR esses dados

sns.displot(film1)
sns.displot(film2)
plt.show()
# as tendencias do conjunto ficaram mais claras, mas essa visualizacao nao eh a ideal para o caso

# eh mais adequado o histograma do Matplotlib
plt.hist(film1)
plt.hist(film2)
plt.show()

# plotagem do boxplot
plt.boxplot([film1, film2])
plt.show()

# esse boxplot a baixo mostra de forma mais clara que as distribuicoes de notas para os dois filmes
# estao seguindo o mesmo comportamento:
plt.boxplot([ratings_toy_story.rating, ratings_jumanji.rating])
plt.show()

# Dessa forma, usar a Matplotlib foi mais pratico ja que os dados ja estao separados
# Mas, o Seaborn permite explorar dados quando ainda nao estao separados

sns.boxplot(x="movieId", y="rating", data=ratings.query("movieId in (1,2)")) # usando a query eu filtro e mostro apenas os dados dos filmes 1 e 2
plt.show()

sns.boxplot(x="movieId", y="rating", data=ratings.query("movieId in (1,2,3,4,5)")) # outro exemplo
plt.show()

############## Desvio Padrao ##############

# Eh uma maneira numerica de verificar o quao distantes estao os outros pontos dessas medidas centrais

print("Jumanjis's Standard Deviation: %.2f" % ratings_jumanji.rating.std(),
      "\nToy Story's Standard Deviation: %.2f" % ratings_toy_story.rating.std())

# Eh possivel notar como o desvio padrao eh muito maior, mesmo com as medias e medianas sendo iguais
print(np.mean(film1), np.mean(film2))
print(np.std(film1), np.std(film2))
print(np.median(film1), np.median(film2))
