import pandas as pd
import matplotlib.pyplot as plt #quando eu colo o "as" ai uso oq coloquei depois dele para referenciar a biblio
import seaborn as sns

#a biblioteca seaborn tbm é uma opção

notas = pd.read_csv("ratings.csv")

#notas.head()
#print(notas)
#print(notas.shape)
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
#print(notas.head) #pandas dataframe

#pandas series:
#print(notas['nota'].unique()) #informa quais foram as notas
#print(notas['nota'].value_counts()) #informa quantas vezes cada nota foi dada e ordenou do mais frequente para o menos
#print(notas['nota'].mean()) #informa a média

n = notas.nota
n_mean = n.mean()
n_median = n.median()
#print(notas.nota)
#n.matplotlib.pyplot.plot(kind='hist')
#matplotlib.pyplot.show()
plt.hist(n) #plota oq eu quero, cria tabela
plt.show() #mostra a tabela

print(n.describe()) #descreve as medidas
sns.boxplot(n) #cria o boxplot
plt.show() #display do boxplot