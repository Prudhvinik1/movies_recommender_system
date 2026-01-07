import streamlit as st
import pandas as pd
import pickle
import requests

api_key = '0c69152ad4ec531692bebe73af82c983'

def fetch_poster(movie_id):
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


# Load Pickle Files
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))



def recommend(movie):

    # Fetch the current movie index
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    # Sort the 5 most similar movies 
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movie_posters

st.title('Movie Recommender System')



selected_movie = st.selectbox(
    'Pick a movie to get Recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations,recommendation_posters = recommend(selected_movie)
    
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.image(recommendation_posters[i])
            st.text(recommendations[i])
            