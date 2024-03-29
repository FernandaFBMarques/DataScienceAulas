import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

print(movies.head(2))

toy_story_ratings = ratings.query("movieId==1")
jumanji_ratings = ratings.query("movieId==2")
print("Toy Story's Ratings: ", len(toy_story_ratings), "\nJumanji's Ratings: ", len(jumanji_ratings))

print("\nToy Story's Average ratings: %.2f" % toy_story_ratings.rating.mean(),
      "\nJumanji's Average ratings: %.2f" % jumanji_ratings.rating.mean())

print("\nToy Story's Standard Deviation: %.2f" % toy_story_ratings.rating.std(),
      "\nJumanji's Standard Deviation: %.2f" % jumanji_ratings.rating.std())

print("\nToy Story's Median: %.2f" % toy_story_ratings.rating.median(),
      "\nJumanji's Median: %.2f" % jumanji_ratings.rating.median())

movie1 = np.append(np.array([2.5] * 10), np.array([3.5] * 10))
movie2 = np.append(np.array([5] * 10), np.array([1] * 10))

print("\nMovie's 1 Average ratings", movie1.mean(), "\nMovie's 2 Average ratings", movie2.mean())
print("\nMovie's 1 Standard Deviation", np.std(movie1),  "\nMovie's 2 Standard Deviation", np.std(movie2))
print("\nMovie's 1 Median", np.median(movie1), "\nMovie's 2 Median", np.median(movie2))

plt.hist(movie1)
plt.hist(movie2)
plt.show()

plt.boxplot([movie1, movie2])
plt.show()
