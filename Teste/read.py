import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Título do app
st.title('Dashboard com Base de Dados')

# Carregar arquivo de dados
file = st.file_uploader("Carregar arquivo CSV", type=['csv'])

st.set_option('deprecation.showPyplotGlobalUse', False)
# Se o arquivo for carregado
if file is not None:
    # Tente ler o arquivo CSV em um DataFrame Pandas
    try:
        data = pd.read_csv(file)
        
        # Mostra os dados na tabela
        st.write("Dados do arquivo CSV:")
        st.write(data)
        
        # Opções do dashboard
        st.sidebar.header('Opções do Dashboard')
        
        # Gráfico de barras
        if st.sidebar.checkbox('Gráfico de Barras'):
            st.subheader('Gráfico de Barras')
            selected_column = st.selectbox('Selecione a coluna:', data.columns)
            plt.figure(figsize=(10, 6))
            sns.countplot(x=selected_column, data=data)
            st.pyplot()

        # Histograma
        if st.sidebar.checkbox('Histograma'):
            st.subheader('Histograma')
            selected_column = st.selectbox('Selecione a coluna:', data.columns)
            plt.figure(figsize=(10, 6))
            sns.histplot(data[selected_column], kde=True)
            st.pyplot()

    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
else:
    st.warning("Por favor, carregue um arquivo CSV.")
