import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tmdb = pd.read_csv("tmdb_5000_movies.csv")

tmdb["original_language"].value_counts().index

tmdb["original_language"].value_counts().values

print(tmdb["original_language"])
print(tmdb["original_language"].value_counts()) # o retorno é uma série pq so tem uma coluna,
# ["en", "fr"...] -> são o index e [4505, 70, 32,...] -> são os valores

print(tmdb["original_language"].value_counts().to_frame()) # ao usar a função to_frame() ele retorna um dataframe

language_count = tmdb["original_language"].value_counts().to_frame().reset_index() # en fr es -> deixam de ser o index e ele os substitui por um contador
language_count.columns = ["original_language", "total"]
print(language_count.head())

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

####################### aula05: #########################
# a query eh uma pergunta
total_per_language_others = tmdb.query("original_language != 'en'").original_language.value_counts() # eu quero as linhas onde a lingua n eh o ingles
print(total_per_language_others)

films_no_original_language_en = tmdb.query("original_language != 'en'")
sns.catplot(x="original_language", kind="count", data=films_no_original_language_en)

# 1º gero a figura
# plt.figure(figsize=(5,10))# o plt.figure() n serve pra catplot
sns.catplot(x="original_language", kind="count", data=films_no_original_language_en,
            aspect=2,
            # WARNING: Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
            palette="GnBu_d",
            order=total_per_language_others.index) # a função catplot e mais altonivel, ele vai chamar a função countplot
# por isso passo o parâmetro
plt.show()

# A MENSAGEM QUE EU QUERO PASSAR AQUI EH QUAL FOI MAIS POPULAR E QUAL FOI MENOS