import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a078695a307dbcaf7935a8b446543b8b&language=en-US'.format(movie_id))
    data=response.json()
    
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500/" + poster_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    #st.write(f"Movie Index: {movie_index}")  # Debug: Show the movie index
    distances = similarity[movie_index]
    #st.write(f"Distances: {distances[:10]}")  # Debug: Show the first 10 distance scores

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    #st.write(f"Movies List: {movies_list}")  # Debug: Show the indices and scores of similar movies


    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id   #fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity_matrix.pkl','rb'))



st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    "Which movie would you like to choose?",
    movies['title'].values)

if st.button("Recommend"):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])










