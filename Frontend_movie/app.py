import streamlit as st
import pandas as pd
import pickle

# Function to recommend movies
def recommend(selected_moviename):
    # Load similarity matrix from pickle (replace with your actual similarity data)
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    # Load movies DataFrame from pickle
    movies = pickle.load(open('movie.pkl', 'rb'))

    # Find index of selected movie in the movies list
    movie_index = movies[movies['title'] == selected_moviename].index[0]

    # Get distances (similarity scores) for the selected movie
    distances = similarity[movie_index]

    # Sort distances and get top 5 recommendations
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id=i[0]
        #Fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

# Streamlit app title
st.title('Movie Recommender System')

# Load movies list from pickle
movies_list = pickle.load(open('movie.pkl', 'rb'))
movies_list = movies_list['title'].values

# Selectbox to choose a movie
selected_moviename = st.selectbox(
    'Select a movie:',
    movies_list
)

# Button to trigger recommendation
if st.button('Recommend'):
    recommendations = recommend(selected_moviename)
    for movie in recommendations:
        st.write(movie)
