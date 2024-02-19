import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tmdb = pd.read_csv("tmdb_5000_movies.csv")

total_per_language = tmdb["original_language"].value_counts() # conta os valores das categorias (linguas) que existem no CSV
overall_total = total_per_language.sum() # soma desses valores
total_en = total_per_language.loc["en"] # guardo nessa variavel os filmes cuja a lingua eh ingles

remaining_total = overall_total - total_en
print(total_en, remaining_total)

data_ = { # dicionario do pandas com duas colunas lingua e totsl
    'language': ['English', 'Others'],
    'total': [total_en, remaining_total]
}
data_ = pd.DataFrame(data_) # gero um dataframe com esse dicionario

sns.barplot(x="language", y="total", data=data_) # ploto um grafico de barras, eixo x -> linguas, eixo y -> ocorrencias no conjunto

total_per_language_others = tmdb.query("original_language != 'en'").original_language.value_counts() # a variavel recebe uma query e retorna todos os valores dif de en

films_no_original_language_en = tmdb.query("original_language != 'en' ") # recebe apenas o conjunto de dados dessas linguas
sns.catplot(x="original_language", kind="count", data=films_no_original_language_en)

sns.catplot(x="original_language", kind="count", data=films_no_original_language_en,
            aspect=2,
            hue="original_language",
            palette="GnBu_d",
            order=total_per_language_others.index,
            legend=False)

plt.show()

