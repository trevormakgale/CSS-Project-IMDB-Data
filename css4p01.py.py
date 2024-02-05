# -*- coding: utf-8 -*-
print("""
======================================================================================================================================
--------------------------------------------------------------------------------------------------------------------------------------
      Created on Sun Feb  4 14:18:49 2024

@author: TT Makgale
        ============
        
        
        CSS Project - Option 1: IMDB Data
       ===================================
       
""")
import pandas as pd

print('Processing Data: IMDB Data ')
print('---------------------------\n')

df = pd.read_csv("movie_dataset.csv")

# 1. Use the Rank column as the index
df1 = pd.read_csv("movie_dataset.csv", index_col=['Rank'])

# 2. Dealing with NA values by removing their entire cells
df1.dropna(inplace=True)

# 3. Question (1) Highest rated
print('# Question (1) Highest rated')
print('The highest film rating: ', df['Rating'].max())
print(df['Title'][df['Rating'] == df['Rating'].max()])

print('\n')
# 4. Question (2) Average revenue of all movies (Except NA)
print('# Question (2) Average revenue of all movies (Except NA)')
print('The average revenue of all movies: ', df['Revenue (Millions)'].mean(),' millions')

print('\n')
# 5. Question (3) Average revenue of movies from 2015 to 2017 in the dataset
print('# Question (3) Average revenue of movies from 2015 to 2017 in the dataset')
print('The average revenue of movies from 2015 to 2017: ',df['Revenue (Millions)'][df['Year'] > 2015].mean(), ' millions')

print('\n')
# 6. Question (4) Movies released in the year 2016
print('Question (4) Movies released in the year 2016:')
print(df['Title'][df['Year'] == 2016].count())

print('\n')
# 7. Question (5) Movies directed by Christopher Nolan
print('Question (5) Movies directed by Christopher Nolan:')
print(df['Title'][df['Director'] == 'Christopher Nolan'].count())

print('\n')
# 8. Question (6) Movies in the dataset that have a rating of at least 8.0
print('Question (6) Movies in the dataset that have a rating of at least 8.0:')
print(df['Title'][df['Rating'] >= 8.0].count())

print('\n')
# 9. Question (7) The median rating of movies directed by Christopher Nolan
print('Question (7) The median rating of movies directed by Christopher Nolan:')
print(df['Rating'][df['Director'] == 'Christopher Nolan'].median())

print('\n')
# 10. Question (8) The year with the highest average rating
print('Question (8) The year with the highest average rating:')
print(df['Year'][df['Rating'] == df['Rating'].max()])

print('\n')
A = df1['Title'][df1['Year'] == 2006].count()
B = df1['Title'][df1['Year'] == 2016].count()
C = ((B - A)/df1['Year'].count())*100
# 11. Question (9) The percentage increase in number of movies made between 2006 and 2016
print('Question (9) The percentage increase in number of movies made between 2006 and 2016')
print(C)

print('\n')
# The hints/tips helped here !!!!!! :0
actors = pd.Series([actor.strip() for actors in df['Actors'].str.split(',') for actor in actors])
# 12. Question (10)The most common actor in all the movies
print('Question (10) The most common actor in all the movies:')
print(actors.value_counts().idxmax())

print('\n')
# The hints/tips helped here too !!!!!! :0
genres = pd.Series([genre.strip() for genres in df['Genre'].str.split(',') for genre in genres])
# 13. Question (11) Unique genres in the dataset
print('Question (11) Unique genres in the dataset:')
print(genres.value_counts().count())

print('\n')
# 14. Question (12) A correlation of the numerical features, what insights that can be deduced
# And 5 insights that can be made.
print("""Question (12) A correlation of the numerical features, what insights that can be deduced and 5 insights that can be made.""")

# imports !!!
import matplotlib.pyplot as plt 
import seaborn as sns        

# Creating a DataFrame with the numerical columns of our movies_dataset to do some correlation measurements on
data = {
    'Year': df1['Year'],
    'Runtime (Minutes)': df1['Runtime (Minutes)'],
    'Rating': df1['Rating'],
    'Votes': df1['Votes'],
    'Revenue (Millions)': df1['Revenue (Millions)'],
    'Metascore': df1['Metascore']}

df2 = pd.DataFrame(data)

# Calculate correlation matrix
correlation_matrix = df2.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix of Numerical Features')
plt.show()

print("""
                               # Insights
                              ============
# 1. Positive correlation: If coefficient is close to 1, features move together. (Red in the figure)
From the figure: Votes seem to correlate well with both Ratings and Revenues. Ratings also seem to correlate with Metascoring.
        
# 2. Negative correlation: If coefficient is close to -1, features move in opposite directions. (Blue in the figure)
From the figure: Year seems to have a negative correlation with all the other features, with the most negative correlation observed with votes.

# 3. Close to 0: Weak or no linear correlation between features.
From the figure: Weak or no linear correlation is observed for Revenue with both Rating and Metascoring. Another weak correlation is observed between Revenue and Runtime, Metascoring and Votes, and finally Runtime with Votes.

# 4. Diagonal elements: Always 1 as it represents the correlation of a feature with itself.

                               # Advice
                              ============
High grossing movies - in terms of Revenue, are most likely to get most votes for various awards - including The Academy Awards. However, note that these votes will not increase every year, as one would expect.                            

====================================================================================================================================== 
    """)