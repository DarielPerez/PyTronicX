#import matplotlib
import pandas as pd
#import xlsx

#Archivo CSV partes del cuerpo afectadas

#Numero de casos accidentes y enfermedades -> segmento 001
a001_2020 = pd.read_csv("Listados CSV\\a001 2020.csv",index_col= 0) #FUNCIONA
a001_2021 = pd.read_csv("Listados CSV\\a001 2021.csv") #FUNCIONA
a001_2022 = pd.read_csv("Listados CSV\\a001 2022.csv") #FUNCIONA
a001_2023 = pd.read_csv("Listados CSV\\a001 2023.csv") #FUNCIONA

#Numero de casos por genero -> segmento 002
a002_2020 = pd.read_csv("Listados CSV\\a002 2020.csv") #FUNCIONA
a002_2021 = pd.read_csv("Listados CSV\\a002 2021.csv") #FUNCIONA
a002_2022 = pd.read_csv("Listados CSV\\a002 2022.csv") #FUNCIONA
a002_2023 = pd.read_csv("Listados CSV\\a002 2023.csv") #FUNCIONA

#Numero de casos por provincia -> segmento 007
a007_2020 = pd.read_csv("Listados CSV\\a007 2020.csv") #FUNCIONA
a007_2021 = pd.read_csv("Listados CSV\\a007 2021.csv") #FUNCIONA
a007_2022 = pd.read_csv("Listados CSV\\a007 2022.csv") #FUNCIONA
a007_2023 = pd.read_csv("Listados CSV\\a007 2023.csv") #FUNCIONA

#Numero de casos por actividad economica -> segmento 008
a008_2020 = pd.read_csv("Listados CSV\\a008 2020.csv") #FUNCIONA
a008_2021 = pd.read_csv("Listados CSV\\a008 2021.csv") #FUNCIONA
a008_2022 = pd.read_csv("Listados CSV\\a008 2022.csv") #FUNCIONA
a008_2023 = pd.read_csv("Listados CSV\\a008 2023.csv") #FUNCIONA

#Numero de casos por actividad economica -> segmento 009
a009_2020 = pd.read_csv("Listados CSV\\a009 2020.csv") #FUNCIONA
a009_2021 = pd.read_csv("Listados CSV\\a009 2021.csv") #FUNCIONA
a009_2022 = pd.read_csv("Listados CSV\\a009 2022.csv") #FUNCIONA
a009_2023 = pd.read_csv("Listados CSV\\a009 2023.csv") #FUNCIONA

#Numero de casos por tipo de empresa -> segmento 010
a010_2020 = pd.read_csv("Listados CSV\\a010 2020.csv") #FUNCIONA
a010_2021 = pd.read_csv("Listados CSV\\a010 2021.csv") #FUNCIONA
a010_2022 = pd.read_csv("Listados CSV\\a010 2022.csv") #FUNCIONA
a010_2023 = pd.read_csv("Listados CSV\\a010 2023.csv") #FUNCIONA

#Numero de casos por grupo de ocupacion -> segmento 012
a012_2020 = pd.read_csv("Listados CSV\\a012 2020.csv") #FUNCIONA
a012_2021 = pd.read_csv("Listados CSV\\a012 2021.csv") #FUNCIONA
a012_2022 = pd.read_csv("Listados CSV\\a012 2022.csv") #FUNCIONA
a012_2023 = pd.read_csv("Listados CSV\\a012 2023.csv") #FUNCIONA

#Tupla con todos los CSV
lista = [a001_2020,a001_2021,a001_2022,a001_2023,
         a002_2020,a002_2021,a002_2022,a002_2023,
         a007_2020,a007_2021,a007_2022,a007_2023,
         a008_2020,a008_2021,a008_2022,a008_2023,
         a009_2020,a009_2021,a009_2022,a009_2023,
         a010_2020,a010_2021,a010_2022,a010_2023,
         a012_2020,a012_2021,a012_2022,a012_2023         
        ]

lista_enfermedades = []
print(a001_2020[["MES"]])
'''
for i in range(len(lista)-1):
    if lista[i][["AT"]]:
        lista_enfermedades.append(lista[i])

print(lista_enfermedades)'''
''''
lista_new = []
#Convertir cada dato en un data frame
def DataFrame(tupla):
    for i in range(len(tupla)-1):
        i = pd.DataFrame(tupla[i])
    return tupla



for i in range(len(lista)-1):
    print(i)
    if (len(lista[i]) < 33):
        lista.pop(i)
        i-=1

print(lista)

def Deletedata(tupla):
    for i in range(len(lista)-1,-1,-1):
        if (len(lista[i]) < 33):
            lista.pop(i)
        break
    return tupla

#lista_new = Deletedata(lista)
print(len(lista))

lista_new = DataFrame(lista)
print(len(lista))

print(len(lista))
#print(len(lista[1]))
'''
''' [ Depuracion de los datos declinados en el CSV de las partes del cuerpo] '''
# lectura de datos
'''
datos = pd.read_csv('Listados CSV/Partes del cuerpo.csv')

# filtro
datos_declinados = datos[datos['Estado'] == 'declinado']
datos_calificados = datos[datos['Estado'] == 'calificado']
datos_proceso_calificacion = datos[datos['Estado']
                                   == 'proceso de calificacion']
# decido donde la voy a guardar
ruta_csv_declinados = 'Listados CSV/declinado.csv'
ruta_csv_calificados = 'Listados CSV/calificado.csv'
ruta_csv_proceso_calificacion = "Listados CSV/proceso_calificacion.csv"

# Guardar datos declinados en otro archivo CSV
datos_declinados.to_csv(ruta_csv_declinados, index=False)
datos_calificados.to_csv(ruta_csv_calificados, index=False)
datos_proceso_calificacion.to_csv(ruta_csv_proceso_calificacion, index=False)
'''

'''
def DepurarDatosNulos(tupla):
    lista_de_nulos = []
    for i in range(len(tupla)-1):
        lista_de_nulos.append(tupla[i].isnull().sum())
    return lista_de_nulos

Datos_nulos = DepurarDatosNulos(Tupla)'''




