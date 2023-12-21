import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Fuel_Consumption.csv")


def show_explore_page_CO2():
    st.title("Explorer les données d’entrainement.")

    st.write(
        """
    #### Appercu des données d'entrainement du model
    """
    )
    st.write(f"Dimensions : {df.shape}")
    st.dataframe(df.head())
    st.write("La description du dataFrame:")
    st.write(df.describe())


df_iphone = pd.read_csv("iphone_purchase_records.csv")

def show_explore_page_iphone():
    st.title("Explorer les données d’entrainement.")

    st.write(
        """
    #### Appercu des données d'entrainement du model
    """
    )
    st.write(f"Dimensions : {df_iphone.shape}")
    st.dataframe(df_iphone.head())
    st.write("La description du dataFrame:")
    st.write(df_iphone.describe())

