import streamlit as st
import pickle
import pandas as pd
import hydralit_components as hc
st.set_page_config(layout='wide')

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# specify the primary menu definition
menu_data = [
        {'icon': "far fa-copy", 'label':"About Us"}
]
over_theme = {'txc_inactive': '#FFFFFF','menu_background':'#2d87f4'}
menu_id = hc.nav_bar(menu_definition=menu_data,home_name='Home',override_theme=over_theme)

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
"How would you like to be contacted?",
movies['title'].values,placeholder="Movie name",index=None)

# st.write("You selected:", option)
# st.button("Reset", type="primary")
if st.button("Recommend"):
    name = recommend(selected_movie_name)
    for i in range(0,5):
        st.write(name[i])