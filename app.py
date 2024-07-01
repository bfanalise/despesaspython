import streamlit as st
import pandas as pd
import time as tm
import math
import plotly.express as px

# Definição de tela
st.set_page_config(page_title='Cadastro de despesas', layout='centered')

# Título da página
st.title('Controle')

# Divisão do titulo para o formulário
st.divider()

# Colunas
coluna1, coluna2 = st.columns([1, 1])

# Início do formulário
with coluna1:
    with st.form(key='despesas', clear_on_submit=True):
        descricao = st.text_input('Descrição')
        valor = st.number_input('Valor')
        origem = st.text_input('Origem')
        competencia = st.date_input('Competência')
        submit_button = st.form_submit_button('Cadastrar')

        if submit_button:
            # Ler o arquivo Excel existente
            arquivo_path = './despesas.xlsx'
            try:
                df = pd.read_excel(arquivo_path)
            except FileNotFoundError:
                df = pd.DataFrame(columns=['Descrição', 'Valor', 'Origem', 'Competência'])

            # Adicionar a nova linha ao DataFrame
            nova_linha = pd.DataFrame({
                'Descrição': [descricao],
                'Valor': [valor],
                'Origem': [origem],
                'Competência': [competencia]
            })
            df = pd.concat([df, nova_linha], ignore_index=True)

            # Salvar o DataFrame atualizado de volta ao arquivo Excel
            df.to_excel(arquivo_path, index=False)

            st.success('Despesa cadastrada com sucesso!')

with coluna2:
    # Ler e exibir o arquivo Excel atualizado
    arquivo_path = './despesas.xlsx'
    try:
        df = pd.read_excel(arquivo_path)
        st.dataframe(df)
    except FileNotFoundError:
        st.write("Ainda não há despesas cadastradas.")
