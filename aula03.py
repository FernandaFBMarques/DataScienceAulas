import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tmdb = pd.read_csv("tmdb_5000_movies.csv")
print(tmdb)
print(tmdb.original_language.unique())# original language é uma categorica nominal
