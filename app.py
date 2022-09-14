import streamlit as st
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#streamlit run app.py
# pip install streamlit --upgrade


st.title('ANALISIS COLEGIOS OFCIALES PEREIRA')

icfes_ris = pd.read_csv('/home/garciautp/Documentos/BD/ICFES/icfes_ris.csv')

filtro = icfes_ris.COLE_MCPIO_UBICACION == 'PEREIRA'
icfes_per = icfes_ris[filtro]
fill = icfes_per.COLE_NATURALEZA == 'OFICIAL'
per_priv = icfes_per[fill]

ls_colegios = per_priv.COLE_NOMBRE_ESTABLECIMIENTO.unique()

seleccion = st.sidebar.selectbox('COLEGIOS:', ls_colegios)

st.write(f'Has seleccionado {seleccion}')
fil2 = per_priv.COLE_NOMBRE_ESTABLECIMIENTO == seleccion
colegio = per_priv[fil2]

puntajes = {
           'Areas': ['LECTURA_CRITICA', 'MATEMATICAS', 'NATURALES', 'SOCIALES', 'INGLES'],
           'Promedio': [colegio.PUNT_LECTURA_CRITICA.mean(),colegio.PUNT_MATEMATICAS.mean(),colegio.PUNT_C_NATURALES.mean(),colegio.PUNT_SOCIALES_CIUDADANAS.mean(),colegio.PUNT_INGLES.mean()]
}
tabla_Inicial = pd.DataFrame(puntajes)

st.write('Datos sin Procesar')
st.write(tabla_Inicial)

#Calculo de valores reales

#MATEMATICAS
Q1 = colegio.PUNT_MATEMATICAS.quantile(0.25)
Q3 = colegio.PUNT_MATEMATICAS.quantile(0.75)
IQR = Q3 - Q1
lim_sup = Q3 +(IQR*1.5)
lim_inf = Q1 - (IQR*1.5)
f5 = colegio.PUNT_MATEMATICAS <= lim_sup
f6 = colegio.PUNT_MATEMATICAS >= lim_inf
mat_tip = colegio[f5 & f6]

#LECTURA_CRITICA
Q1 = colegio.PUNT_LECTURA_CRITICA.quantile(0.25)
Q3 = colegio.PUNT_LECTURA_CRITICA.quantile(0.75)
IQR = Q3 - Q1
lim_sup = Q3 +(IQR*1.5)
lim_inf = Q1 - (IQR*1.5)
f5 = colegio.PUNT_LECTURA_CRITICA <= lim_sup
f6 = colegio.PUNT_LECTURA_CRITICA >= lim_inf
lec_tip = colegio[f5 & f6]

#CIENCIAS NATURALES
Q1 = colegio.PUNT_C_NATURALES.quantile(0.25)
Q3 = colegio.PUNT_C_NATURALES.quantile(0.75)
IQR = Q3 - Q1
lim_sup = Q3 +(IQR*1.5)
lim_inf = Q1 - (IQR*1.5)
f5 = colegio.PUNT_C_NATURALES <= lim_sup
f6 = colegio.PUNT_C_NATURALES >= lim_inf
nat_tip = colegio[f5 & f6]

#INGLES
Q1 = colegio.PUNT_INGLES.quantile(0.25)
Q3 = colegio.PUNT_INGLES.quantile(0.75)
IQR = Q3 - Q1
lim_sup = Q3 +(IQR*1.5)
lim_inf = Q1 - (IQR*1.5)
f5 = colegio.PUNT_INGLES <= lim_sup
f6 = colegio.PUNT_INGLES >= lim_inf
ing_tip = colegio[f5 & f6]

#SOCIALES
Q1 = colegio.PUNT_SOCIALES_CIUDADANAS.quantile(0.25)
Q3 = colegio.PUNT_SOCIALES_CIUDADANAS.quantile(0.75)
IQR = Q3 - Q1
lim_sup = Q3 +(IQR*1.5)
lim_inf = Q1 - (IQR*1.5)
f5 = colegio.PUNT_SOCIALES_CIUDADANAS <= lim_sup
f6 = colegio.PUNT_SOCIALES_CIUDADANAS >= lim_inf
soc_tip = colegio[f5 & f6]

puntajesProc = {
           'Areas': ['LECTURA_CRITICA', 'MATEMATICAS', 'NATURALES', 'SOCIALES', 'INGLES'],
           'Promedio': [lec_tip.PUNT_LECTURA_CRITICA.mean(),mat_tip.PUNT_MATEMATICAS.mean(),nat_tip.PUNT_C_NATURALES.mean(),soc_tip.PUNT_SOCIALES_CIUDADANAS.mean(),ing_tip.PUNT_INGLES.mean()]
}
tabla_Process = pd.DataFrame(puntajesProc)

st.write('Datos Procesados')
st.write(tabla_Process)
