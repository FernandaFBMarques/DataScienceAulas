import pandas as pd

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

print(movies.head())
print(ratings.query("movieId==1").rating)# mostra as notas somente do filme 1, ao colocar . rating no final ele so mostra a nota se eu tiro ele coloca todas as infos do filme 1
meanR1 = (ratings.query("movieId==1").rating.mean())
print("Mean rating movie 1 = ", meanR1)
#PAREI NO MIN 4:45