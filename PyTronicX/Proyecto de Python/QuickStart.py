




import pandas as pd

datos = pd.read_csv("Proyecto de Python\Partes del cuerpo.csv",header=0)

#
print(datos) #Imprimimos todos los datos

#Imprimir datos de una sola columna
#print(datos["Nombre_de_columna"])

#imprimir las 3 primeras filas
print(datos[0:3])

#Acomodar filas con relacion a los datos de una columna
#print(datos.sort_values(by='nombre_de_la_columna'))

#Acomodar filas con relacion a los datos de una columna menor a mayor
#print(datos.sort_values(by='nombre_de_la_columna',ascending=False))

#ver datos que cumplan con x condicion
print(datos[datos[:0]<10])