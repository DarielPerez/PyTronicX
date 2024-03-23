

import pandas as pd
import cufflinks as cf
import plotly as pl
from IPython.display import display, HTML

cf.set_config_file(sharing="public",theme="ggplot",offline="True")
#Configuracion, compartido publico, tema blanco, y en modo offline'

#Conocer todos los temas disponibles
#cf.getTheme()

df = pd.read_csv("PyTronicX\\population_total.csv")
df = df.dropna() #Eliminar datos nulos

#metodo pivot
#index: Los indices obtendran el valor de los años
#columns:  Representará a los paises, es decir, cada pais será una columna
#values:    y cada columna obtendra su respectivo valor de poblacion
df = df.pivot(index="year",columns="country",values="population")

#elegiré solo 5 paises
df = df[["United States","India","China","Indonesia","Brazil"]]

###########################################################################
#LinePlot
df.iplot(kind="line")
print(df)

