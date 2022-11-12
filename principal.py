import streamlit as st
from sklearn.naive_bayes import GaussianNB
import pandas as pd

dados = pd.read_csv('bolos')



st.title('Aplicativo para compra de bolos da Marcia')
st.image('Marciel.PNG')
SepalLengthCm = st.number_input('bolo cenoura')
st.image('Marciel.PNG')
SepalWidthCm = st.number_input('bolo de limão')
st.image('Marciel.PNG')


 
