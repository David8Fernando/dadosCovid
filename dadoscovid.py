import pandas as pd
import plotly.express as px
import streamlit as st 

#streamlit run codigoBase.py

#LENDO O DATASET
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#MELHORANDO O NOME DAS COLUNAS DA TABELA
df = df.rename(columns={'newDeaths': 'Novos óbitos','newCases': 'Novos casos','deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes','totalCases_per_100k_inhabitants':'Casos por 100 mil habitantes'})

#SELECÃO DO ESTADO
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Qual estado?', estados) #Menu lateral

# Filtra o DataFrame pelo estado selecionado
df_estado = df[df['state'] == state]



# SELEÇÃO DA COLUNA DE DADOS
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)

st.sidebar.link_button("Meu Linkedin", "https://www.linkedin.com/in/davidfernandopereira/")
st.sidebar.link_button("Github", "https://github.com/David8Fernando")


# Cálculo dos totais
Totaldecasos = df_estado['totalCases'].sum()
Totaldeobitos = df_estado['deaths'].sum()
Totalderecup = df_estado['recovered'].sum()

Totaldecasos_fmt = "{:,.0f}".format(Totaldecasos).replace(",", ".")
Totaldeobitos_fmt = "{:,.0f}".format(Totaldeobitos).replace(",", ".")
Totalderecup_fmt = "{:,.0f}".format(Totalderecup).replace(",", ".")



st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem.')


# Criando um estilo CSS para aumentar o tamanho das métricas
def metric_card(label, value):
    st.markdown(
        f"""
        <div style="
            background-color: #f0f2f6;
            padding: 10px 8px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            width: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
        ">
            <h4 style="margin: 0; color: #333; font-weight: bold; font-size: 18px;">{label}</h4>
            <h2 style="margin: 5px 0; color: #007BFF; font-size: 28px; font-weight: bold;">{value}</h2>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Formatação dos números
Totaldecasos_fmt = "{:,.0f}".format(Totaldecasos).replace(",", ".")
Totaldeobitos_fmt = "{:,.0f}".format(Totaldeobitos).replace(",", ".")
Totalderecup_fmt = "{:,.0f}".format(Totalderecup).replace(",", ".")

# Criando layout com 3 colunas e métricas personalizadas
col1, col2, col3 = st.columns(3)

with col1:
    metric_card("Total de casos", Totaldecasos_fmt)

with col2:
    metric_card("Total de óbitos", Totaldeobitos_fmt)

with col3:
    metric_card("Total de recuperados", Totalderecup_fmt)





fig = px.line(df, x="date", y=column, title=f'{column} - {state}')
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})


st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')



