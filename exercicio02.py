import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")

# vamos, inicialmente, mostrar graficamente nossos dados.

ratings.rating.plot(kind='hist') # defino o tipo do gráfico, que será um histograma de notas, selecionando a coluna rating e aplicando o argumento kind
print(ratings.rating.describe())# mostro as descrições dos dados de nota

# agora a parte VISUAL

# importo o Seaborn, o responsável por mostrar a imagem na tela
sns.boxplot(ratings.rating) # atribuo ratings.rating para a função boxplot()
plt.show()

mean_movie_rating = ratings.groupby("movieId").mean().rating # forma de obter a média de cada um dos filmeID sem ter que digitar o comando várias vezes
# para obter a média das notas, pega o grupo dela e faz o calculo das médias, mostra os 5 primeiros
plt.hist(mean_movie_rating) # uso o plt para fazer o histograma
plt.title("Movie average histogram")
plt.show()
