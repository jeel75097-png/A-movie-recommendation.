import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies_data = pd.read_csv('movies.csv')

# Features used for recommendation
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

# Fill empty values
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# Combine features
combined_features = (
    movies_data['genres'] + ' ' +
    movies_data['keywords'] + ' ' +
    movies_data['tagline'] + ' ' +
    movies_data['cast'] + ' ' +
    movies_data['director']
)

# Convert text into vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Similarity calculation
similarity = cosine_similarity(feature_vectors)

# User input
movie_name = input('Enter your favourite movie name: ')

# Get all movie titles
list_of_all_titles = movies_data['title'].tolist()

# Find closest movie name
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

if len(find_close_match) == 0:
    print("Movie not found")
else:
    close_match = find_close_match[0]

    # Movie index
    index_of_movie = movies_data[movies_data.title == close_match].index[0]

    # Similarity scores
    similarity_score = list(enumerate(similarity[index_of_movie]))

    # Sort movies
    sorted_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    print("\nMovies Suggested For You:\n")

    i = 1
    for movie in sorted_movies:
        index = movie[0]
        title = movies_data.iloc[index]['title']

        if i <= 20:
            print(i, ".", title)
            i += 1