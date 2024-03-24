import pandas as pd
import matplotlib.pyplot as plt
# Lee el archivo CSV
df = pd.read_csv("Listados CSV\\Partes del cuerpo.csv")

# Divide cada valor de la columna por la coma y selecciona solo la primera parte
df['Parte_Lesion'] = df['Parte_Lesion'].str.split(',').str[0]

# Guarda el DataFrame actualizado en un nuevo archivo CSV
df.to_csv('Listados CSV\\Partes del cuerpo.csv', index=False, encoding='utf-8-sig')


