'''
Pandas Homework with IMDb data
'''

'''
BASIC LEVEL
'''

import pandas as pd
import matplotlib.pyplot as plt

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_csv('imdb_1000.csv')
# check the number of rows and columns
movies.shape
# check the data type of each column
movies.dtypes
# calculate the average movie duration
movies.duration.mean()
# sort the DataFrame by duration to find the shortest and longest movies
#Longest films
movies.sort('duration',ascending=False)
#Shortest films
movies.sort('duration')
# create a histogram of duration, choosing an "appropriate" number of bins
movies.duration.plot(kind="hist", bins=11, title = "Histogram of Movie duration")
# use a box plot to display that same data
movies.duration.plot(kind="box")
'''
INTERMEDIATE LEVEL
'''
# count how many movies have each of the content ratings

movies.content_rating.value_counts()
# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind="bar")
# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP

movies['content_rating'] = movies.content_rating.map({'NOT RATED':'UNRATED', 'APPROVED':'UNRATED','PASSED':'UNRATED','GP':'UNRATED', 'R':'R', 'PG-13':'PG-13',
                            'PG':'PG','G':'G','NC-17':'NC-17','X':'X','TV-MA':'TV-MA','NaN':'NaN', 'UNRATED': 'UNRATED'})

# convert the following content ratings to "NC-17": X, TV-MA
movies['content_rating'] = movies.content_rating.map({'NOT RATED':'UNRATED', 'APPROVED':'UNRATED','PASSED':'UNRATED','GP':'UNRATED', 'R':'R', 'PG-13':'PG-13',
                            'PG':'PG','G':'G','NC-17':'NC-17','X':'NC-17','TV-MA':'NC-17','NaN':'NaN', 'UNRATED':'UNRATED'})
# count the number of missing values in each column
movies.isnull().sum()

# if there are missing values: examine them, then fill them in with "reasonable" values
movies[movies.content_rating.isnull()]

'''
Question:
Do not know how to replace each one of them.
'''
movies.content_rating.fillna(value='PG', inplace=True)
# calculate the average star rating for movies 2 hours or longer,
movies[movies.duration >= 120].duration.mean()
# and compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration < 120].duration.mean()
# use a visualization to detect whether there is a relationship between duration and star rating
movies.plot(kind = 'scatter', x = 'duration', y = 'star_rating')


# calculate the average duration for each genre

movies.groupby('content_rating').duration.mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration

movies.boxplot(column = 'duration', by = 'content_rating')

# determine the top rated movie (by star rating) for each genre
movies.sort('star_rating', ascending = False).groupby('content_rating').head(1)

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
movies[movies.title.duplicated(take_last = True)]
movies[movies.title.duplicated(take_last = False)]

'''
As we can eyeball, we have different actors etc so they are not actually duplicates.
'''

# calculate the average star rating for each genre, but only include genres with at least 10 movies
'''
I have observed that all the currently categorized genres have at least 10 movies.
I still haven't figured out how to programmatically sort it for at least 10 or rather haven't
spent enough time for it
'''

movies.groupby('content_rating').star_rating.mean()




'''
BONUS
'''

# Figure out something "interesting" using the actors data!
