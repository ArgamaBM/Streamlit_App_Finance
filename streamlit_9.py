import streamlit as st
import quandl

#Recogeremos datos de bolsa como en dash con yahoofinance y quandl
st.title('Gráfica con streamlir para Fiunanzas')

empresas = ("GOOGL","APPL","TSLA","NFLX")

opcion = st.selectbox('Seleccione una de estas empresas:',
                      empresas)

st.write("Has escogido: ",opcion)

años = st.slider("Número de años que quieres plotear", 1,5)
st.write("Has elegido:",años,"años")
año_final = 2015 + años
st.write("año final:", año_final)

data = quandl.get(f'WIKI/{opcion}',
                  start_date="2015-1-1",
                  end_date=f'{año_final}-12-31')

st.write("Vamos a imprimir los 5 primeros valores del dataset")
st.write(data.head())
st.dataframe(data.head())

st.write("Vamos a imprimir los últimos 5 valores del Dataset")
st.write(data.tail())

st.write("Seleccionamos solamente la columna Close")
data = data[['Close']]
st.dataframe(data)

st.write('Vamos a plotear el gráfico selñeccionado')
st.write('Gráfico seleccionado',opcion)
st.write('Año inicial: 2015 ','año final: ',año_final)
st.line_chart(data)


