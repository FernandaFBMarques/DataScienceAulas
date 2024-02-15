import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tmdb = pd.read_csv("tmdb_5000_movies.csv")

print(tmdb["original_language"])
print(tmdb["original_language"].value_counts()) # o retorno é uma série pq so tem uma coluna,
# ["en", "fr"...] -> são o index e [4505, 70, 32,...] -> são os valores

print(tmdb["original_language"].value_counts().to_frame()) # ao usar a função to_frame() ele retorna um dataframe

language_count = tmdb["original_language"].value_counts().to_frame().reset_index() # en fr es -> deixam de ser o index e ele os substitui por um contador
language_count.columns = ["original_language", "total"]
print(language_count.head())

# estou utilizando o seaborn categorical
sns.barplot(x="original_language", y="total", data=language_count)
plt.show()

sns.catplot(x="original_language", kind="count", data=tmdb)
plt.show()

plt.pie(language_count["total"], labels=language_count["original_language"]) # super delicado usar o grafico de torta
plt.show()

total_per_language = tmdb["original_language"].value_counts()
total_amount = total_per_language.sum()
en_total = total_per_language.loc["en"] # uso o loc pq quero identificar onde está o ingles
remaining_total = total_amount - en_total
print(en_total, remaining_total)# agora eu tenho so duas categorias

data_ = {
    'language': ['english', 'others'],
    'total': [en_total, remaining_total]
}
#crio um dataframe em cima desses dados
data_ = pd.DataFrame(data_)

# ploto o meu grafico em cima do dataframe que eu criei
sns.barplot(x="language", y="total", data=data_)
plt.show()

# a query eh uma pergunta
total_per_language_others = tmdb.query("original_language != 'en'") # eu quero as linhas onde a lingua n eh o ingles
print(total_per_language_others)

sns.catplot(x="original_language", kind="count", data=total_per_language_others) #podemos plotar de uma só vez as categorias contidas nesse conjunto
# agrupando as línguas e contando elas
plt.show()
