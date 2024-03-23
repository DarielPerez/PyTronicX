


import pandas as pd

ah = pd.read_csv("Listados CSV\\Partes del cuerpo.csv")
clase = ah[ah["Parte_Lesion"]]
print(clase.head())