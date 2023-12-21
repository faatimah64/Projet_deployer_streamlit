import streamlit as st
import pickle
import numpy as np


def load_model_CO2():
    with open('model.sav', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model_CO2()

def show_predict_page_C02():
    st.title("Prédiction de la quantité de C02 émis par les vehicules.")

    st.write("""Quelques informations necessaires sur le vehicule.""")

    taille_moteur = st.slider("Taille du moteur", 1.0, 10.0, 2.0)
    nbr_cylindre = st.slider("Nombre de cylindres", 1, 20, 5)
    cons_carburant = st.slider("Consommation de carburant", 1.0, 50.0, 10.0)

    click = st.button("Prédire l'émission de C02")
    if click:
        input_data = np.asarray([taille_moteur, nbr_cylindre, cons_carburant]).reshape(1, -1)
        prediction = model.predict(input_data)

        st.subheader(f"La quantité de C02 émis par ce vehicule est estimer à {prediction[0]:.2f}")
    
    with st.sidebar.expander("A propos du model"):
        st.markdown("""

        Après avoir entrainer trois models de régressions avec les données 
        (voir Exploration), le model de *régression linéaire de scikit-learn* 
        semble etre légérement plus performant.

        Il offre le meilleur score **R²** avec la plus petite erreur quadratique moyenne.

        """)






def load_model_iphone():
    with open('model_knn_std.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model_iphone()
standard = data['standard']
model_knn = data['model']

def show_predict_page_iphone():
    st.title("Prédiction de l'achat ou non d'iphone par une personne")

    st.write("""Quelques informations necessaires sur la personne.""")

    gender = st.selectbox('Homme ou Femme', ('Homme', 'Femme'))
    age = st.slider("L'age de la personne", 16, 80, 20)
    salary = st.slider("Le salaire de la personne", 10000, 350000, 20000)

    click = st.button("Est ce que cette personne possède un iphone ?")
    if click:
        g = 1 if gender == 'Homme' else 0
        tab = [[0, 16, 15000], [g, age, salary], [1, 60, 150000]]
        input_data = np.asarray([g, age, salary]).reshape(1, -1)
        input_data = standard.transform(input_data)
        prediction = model_knn.predict(input_data)

        result = "achète un iphone" if prediction[0]==0 else "n'achète pas d'iphone"
        st.subheader(f"Cette personne {result}",)
    
    with st.sidebar.expander("A propos du model"):
        st.markdown("""

        Après avoir entrainer trois models de classification avec les données 
        (voir Exploration), le model de *K-Nearest Neighbours de scikit-learn* 
        semble etre légérement plus performant.

        Il offre le meilleur score **F1** avec le meilleur pourcentage de bonnes prédictions.

        """)