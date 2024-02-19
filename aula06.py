import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tmdb = pd.read_csv("tmdb_5000_movies.csv")
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

ratings_toy_story = ratings.query("movieId==1")
ratings_jumanji = ratings.query("movieId==2")
print(len(ratings_toy_story), len(ratings_jumanji))
print("Toy Story's Average Rating: %.2f" % ratings_toy_story.rating.mean())
print("Jumanji's Average Rating: %.2f" % ratings_jumanji.rating.mean())
