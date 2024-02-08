import pandas as pd # estou importando a biblioteca pandas e a apelidando de pd
import matplotlib.pyplot as plt
import seaborn as sns

notas = pd.read_csv("/Users/mariafernandafreitasbarbosamarques/Desktop/introducao-a-data-science-aula0/aula0/ml-latest-small/ratings.csv") # o Pandas esta lendo o nosso arquivo CSV

print(notas.head()) # mostra os 5 primeiros dados

notas.columns = ["usuarioID", "filmeID", "nota", "momento"] # renomeio as colunas do dataframe para port

print("Dataframe em português: \n",notas.head())

unicas = notas['nota'].unique() # notas repetidas, então vou deixar elas unicas
count = notas['nota'].value_counts() # conto todas elas

mean = notas.nota.mean()
median = notas.nota.median()
print("Notas que aparecem: ",unicas, "\nQuantidade de vezes que aparece cada nota: ", count,
"\nMédia: ",mean, "\nMediana: ",median)

# quantas vezes cada uma das notas apareceu no CSV,
# considerando o total de avaliações feitas pelo usuário.
# ->R: utilizar  método value_counts() das series do pandas

