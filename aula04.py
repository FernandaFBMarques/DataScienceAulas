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

