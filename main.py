import streamlit as st
from predict_page import show_predict_page_C02, show_predict_page_iphone
from explore_page import show_explore_page_CO2, show_explore_page_iphone
from visualisation_page import show_vizualisation_page_CO2, show_vizualisation_page_iphone

project = st.sidebar.selectbox('Projet', ('CO2', "Iphone"))
page = st.sidebar.radio('Sommaire :', ('Prédiction', 'Exploration', 'Visualisation'))

if project == 'CO2':
    if page == 'Prédiction':
        show_predict_page_C02()
    elif page == 'Exploration':
        show_explore_page_CO2()
    else:
        show_vizualisation_page_CO2()
else:
    if page == 'Prédiction':
        show_predict_page_iphone()
    elif page == 'Exploration':
        show_explore_page_iphone()
    else:
        show_vizualisation_page_iphone()
