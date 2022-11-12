import streamlit as st
from sklearn.naive_bayes import GaussianNB
import pandas as pd

dados = pd.read_csv('bolos')

classes = dados['tipos']
nomesColunas = dados.columns.to_list()
tamanho = len(nomesColunas)
nomesColunas = nomesColunas[1:tamanho-1]
features = dados[nomesColunas]

from sklearn.model_selection import train_test_split

features_treino,features_teste,classes_treino,classes_teste = train_test_split(features,
                                                                               classes,
                                                                               test_size=0.26,
                                                                               random_state=3)



model= GaussianNB()


model.fit(features_treino,classes_treino)
predicoes = model.predict(features_teste)


st.title('Aplicativo para compra de bolos da Marcia')
st.image('bolo Marcia.PNG')
SepalLengthCm = st.number_input('qual bolo voce quer')
SepalWidthCm = st.number_input('Digite o tipo de cobertura')

if st.button('Clique aqui'):
  resultado = model.predict([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])

 

 
