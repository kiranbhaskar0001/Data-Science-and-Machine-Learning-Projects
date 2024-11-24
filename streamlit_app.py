import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# Function to add background image to the Streamlit app
def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url('https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

# Function to recommend movies based on selected movie
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = []
    for i in distances[1:11]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

# Streamlit app setup
st.set_page_config(
    page_title="Movie / TV Show Recommender System",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Title and background image
add_bg_from_url()
st.title('🎥 Movie / TV Show Recommender System')

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Movie selection dropdown
selected_movie_name = st.selectbox('Select a Movie', movies['title'].values, help="Choose a movie to get recommendations for.") 

# Recommendation button
if st.button('Get Recommendations'):
    recommended_movie_names = recommend(selected_movie_name)
    
    # Display recommended movie names with index
    st.header("Recommended Movies:")
    if recommended_movie_names:
        for i, movie_name in enumerate(recommended_movie_names, start=1):
            st.subheader(f"{i}. {movie_name}")
    else:
        st.warning("No recommendations found.")
