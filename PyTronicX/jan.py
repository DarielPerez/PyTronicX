import pandas as pd
import csv
import matplotlib.pyplot as plt
import tkinter as ttk

def suma(df,x,z):
    cache_accidente = []                            #Generamos una lista cache para almacenar los datos provicionalmente
    cache_enfermedades = []                         #Generamos una lista cache para almacenar los datos provicionalmente
    for i in range(len(df)):
        df[i] = df[i].dropna()                      #Eliminamos los datos nulos
        cache_accidente.append(df[i][x].sum())      #Sumamos la columna de los accidentes y lo guardamos en los datos cache
        cache_enfermedades.append(df[i][z].sum())   #Sumamos la columna de las enfermedades y lo guardamos en los datos cache
    return cache_accidente,cache_enfermedades       #Retornamos las listas caches

# la ruta original del archivo
ruta_csv_original = "Listados CSV/Partes del cuerpo.csv"

# lectura de datos
datos = pd.read_csv(ruta_csv_original)

# filtro
datos_declinados = datos[datos['Estado'] == 'declinado']

datos_calificados = datos[datos['Estado'] == 'calificado']

datos_proceso_calificacion = datos[datos['Estado'] == 'proceso de calificacion']

# decido donde la voy a guardar
ruta_csv_declinados = "Listados CSV\\declinado.csv"

ruta_csv_calificados = "Listados CSV\\calificado.csv"

ruta_csv_proceso_calificacion = "Listados CSV\\proceso_calificacion.csv"

# Guardar datos declinados en otro archivo CSV
datos_declinados.to_csv(ruta_csv_declinados, index=False)

datos_calificados.to_csv(ruta_csv_calificados, index=False)

datos_proceso_calificacion.to_csv(ruta_csv_proceso_calificacion, index=False)

# lee los datos de calificados
datos_calificados = pd.read_csv(ruta_csv_calificados)

datos_declinados = pd.read_csv(ruta_csv_declinados)

datos_proceso_calificacion = pd.read_csv(ruta_csv_proceso_calificacion)


# Elimina las columnas
datos_calificados = datos_calificados.drop(
    columns=['No_reporte', 'Tipo_Reporte'])

datos_declinados = datos_declinados.drop(
    columns=['No_reporte', 'Tipo_Reporte'])

datos_proceso_calificacion = datos_proceso_calificacion.drop(
    columns=['No_reporte', 'Tipo_Reporte'])


# Guarda los datos modificados
datos_calificados.to_csv(ruta_csv_calificados, index=False)

datos_declinados.to_csv(ruta_csv_declinados, index=False)

datos_proceso_calificacion.to_csv(ruta_csv_proceso_calificacion, index=False)



# Graficar los datos

# Convertir la columna de fechas a formato de fecha
datos_calificados['Fecha_Reg_calific'] = pd.to_datetime(datos_calificados['Fecha_Reg_calific'])

# Crear una nueva columna con el mes y año como cadena de texto
datos_calificados['Mes_Año'] = datos_calificados['Fecha_Reg_calific'].dt.to_period('M').astype(str)

# Agrupar los datos por mes y año y contar la cantidad de datos en cada grupo
datos_agrupados = datos_calificados.groupby('Mes_Año').size().reset_index(name='Cantidad')
"""
#creacion de graficos de barra de los datos calificados por mes del año
plt.figure(figsize=(10, 6))
plt.bar(datos_agrupados['Mes_Año'], datos_agrupados['Cantidad'], color='green', alpha=0.7)
plt.title('Cantidad de datos calificados por mes y año')
plt.xlabel('Mes y Año', fontsize=10)
plt.ylabel('Cantidad', fontsize=10)
plt.xticks(rotation=45, ha='right')
plt.grid(True)
#plt.show()


"""

# Convertir la columna de fechas a formato de fecha
datos_declinados['Fecha_Reg_calific'] = pd.to_datetime(datos_declinados['Fecha_Reg_calific'])
"""
# Crear una nueva columna con el mes y año como cadena de texto
datos_declinados['Mes_Año'] = datos_declinados['Fecha_Reg_calific'].dt.to_period('M').astype(str)

# Agrupar los datos por mes y año y contar la cantidad de datos en cada grupo
datos_agrupados = datos_declinados.groupby('Mes_Año').size().reset_index(name='Cantidad')

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(datos_agrupados['Mes_Año'], datos_agrupados['Cantidad'], color='red', alpha=0.7)
plt.title('Cantidad de datos Declinados por mes y año')
plt.xlabel('Mes y Año', fontsize=10)
plt.ylabel('Cantidad', fontsize=10)
plt.xticks(rotation=45, ha='right')
plt.grid(True)
#plt.show()

# Contar el número de filas calificadas y declinadas
#esto lo toma de los datos generales
datos = pd.read_csv("Listados CSV/Partes del cuerpo.csv")
num_calificados = datos[datos['Estado'] == 'calificado'].shape[0]
num_declinado = datos[datos['Estado'] == 'declinado'].shape[0]
categorias = ['Calificados', 'Declinados']
explode = [0, 0.1]
alturas = [num_calificados, num_declinado]
colores = ['limegreen', 'red']
plt.figure(figsize=(8, 8))  # Tamaño opcional del gráfico
plt.pie(alturas, labels=categorias, colors=colores, autopct='%1.1f%%', startangle=140, 
        wedgeprops = {"linewidth": 1, "edgecolor": "white"}, explode = explode)
plt.axis('equal')
plt.title('Comparación de Calificados y Declinados')
#plt.show() 




columna_interes = 'Parte_Lesion'

# Contar la frecuencia de cada segmento en la columna de interés
frecuencia_segmentos = datos_calificados[columna_interes].value_counts()


segmentos_mas_comunes = frecuencia_segmentos.head(20)

# Graficar 
plt.figure(figsize=(22, 10))
segmentos_mas_comunes.plot(kind='barh', color='skyblue')
plt.title('20 lesiones mas frecuentes de los datos calificados'.format(columna_interes))
plt.xlabel('Frecuencia')
plt.ylabel('Partes del cuerpo')
plt.xticks(rotation=0) 
plt.tight_layout()
#plt.show()"""
""""
columna_interes = 'Parte_Lesion'
#creacion de graficos de barra de los datos calificados por mes del año
plt.figure(figsize=(10, 6))
plt.bar(datos_agrupados['Mes_Año'], datos_agrupados['Cantidad'], color='green', alpha=0.7)
plt.title('Cantidad de datos calificados por mes y año')
plt.xlabel('Mes y Año', fontsize=10)
plt.ylabel('Cantidad', fontsize=10)
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.show()"""
"""
#lo mismo pero con los datos declinados
frecuencia_segmentos = datos_declinados[columna_interes].value_counts()
segmentos_mas_comunes = frecuencia_segmentos.head(20)


plt.figure(figsize=(22, 10))
segmentos_mas_comunes.plot(kind='barh', color='red')
plt.title('20 lesiones mas frecuentes de los datos Declinados'.format(columna_interes))
plt.xlabel('Frecuencia')
plt.ylabel('Partes del cuerpo')
plt.xticks(rotation=0)  
plt.tight_layout()
#plt.show()


#..........................................
#total de casos por tipo de empresas (a010)
#..........................................

# Cargar datos de empresas públicas
archivo1_pub = "Listados CSV\\a010 2020.csv"
archivo2_pub = "Listados CSV\\a010 2021.csv"
archivo3_pub = "Listados CSV\\a010 2022.csv"
archivo4_pub = "Listados CSV\\a010 2023.csv"

# Cargar datos específicos de empresas públicas
datos1_pub = pd.read_csv(archivo1_pub).iloc[1, 13]
datos2_pub = pd.read_csv(archivo2_pub).iloc[1, 13]
datos3_pub = pd.read_csv(archivo3_pub).iloc[1, 13]
datos4_pub = pd.read_csv(archivo4_pub).iloc[1, 13]

# Cargar datos de empresas privadas
archivo1_priv = "Listados CSV\\a010 2020.csv"
archivo2_priv = "Listados CSV\\a010 2021.csv"
archivo3_priv = "Listados CSV\\a010 2022.csv"
archivo4_priv = "Listados CSV\\a010 2023.csv"

# Cargar datos específicos de empresas privadas
datos1_priv = pd.read_csv(archivo1_priv).iloc[0, 13]
datos2_priv = pd.read_csv(archivo2_priv).iloc[0, 13]
datos3_priv = pd.read_csv(archivo3_priv).iloc[0, 13]
datos4_priv = pd.read_csv(archivo4_priv).iloc[0, 13]

# Crear listas para los años y los datos de empresas públicas y privadas
years = ['2020', '2021', '2022', '2023']
public_cases = [datos1_pub, datos2_pub, datos3_pub, datos4_pub]
private_cases = [datos1_priv, datos2_priv, datos3_priv, datos4_priv]

# Crear la figura y los ejes
plt.figure(figsize=(10, 6))

# Graficar los datos de empresas públicas como puntos azules
plt.plot(years, public_cases, color='blue', label='Empresas Públicas', marker='o')

# Graficar los datos de empresas privadas como puntos rojos
plt.plot(years, private_cases, color='red', label='Empresas Privadas', marker='x')

# Añadir etiquetas y título
plt.xlabel('Año')
plt.ylabel('Casos')
plt.title('Total de casos por tipo de empresas (a010) por año')
plt.xticks(years)  # Asegura que todos los años se muestren en el eje x
plt.legend()

# Mostrar la gráfica
plt.grid(True)
#plt.show()

#..........................................
#total de casos por genero (a002)
#..........................................

#Empresas publicas
# Cargar datos de los archivos CSV
archivo1 = "Listados CSV\\a002 2020.csv"
archivo2 = "Listados CSV\\a002 2021.csv"
archivo3 = "Listados CSV\\a002 2022.csv"
archivo4 = "Listados CSV\\a002 2023.csv"

# Cargar datos específicos de cada archivo
datos1 = pd.read_csv(archivo1).iloc[1, 13]  # Selecciona la celda en la primera fila y primera columna
datos2 = pd.read_csv(archivo2).iloc[1, 13]  # Selecciona la celda en la primera fila y primera columna
datos3 = pd.read_csv(archivo3).iloc[1, 13]  # Selecciona la celda en la primera fila y primera columna
datos4 = pd.read_csv(archivo4).iloc[1, 13]  # Selecciona la celda en la primera fila y primera columna

nombres_archivos = ['2020', '2021', '2022', '2023']
valores_celdas = [datos1, datos2, datos3, datos4]

#Empresas privadas

# Cargar datos específicos de cada archivo
datos1_Privadas = pd.read_csv(archivo1).iloc[0, 13]  # Selecciona la celda en la primera fila y primera columna
datos2_Privadas = pd.read_csv(archivo2).iloc[0, 13]  # Selecciona la celda en la primera fila y primera columna
datos3_Privadas  = pd.read_csv(archivo3).iloc[0, 13]  # Selecciona la celda en la primera fila y primera columna
datos4_Privadas  = pd.read_csv(archivo4).iloc[0, 13]  # Selecciona la celda en la primera fila y primera columna

# Crear una figura y ejes
fig, axs = plt.subplots(2)

# Graficar los datos de empresas publicas en el primer conjunto de ejes
axs[0].bar(nombres_archivos, valores_celdas)
axs[0].set_ylabel('Casos')
axs[0].set_title('Total de casos de genero Femenino')

# Graficar los datos de empresas privadas en el segundo conjunto de ejes
axs[1].bar(nombres_archivos, [datos1_Privadas , datos2_Privadas , datos3_Privadas , datos4_Privadas])
axs[1].set_ylabel('Casos')
axs[1].set_title('Total de casos de genero Masculino')

# Ajustar el diseño de la figura
plt.tight_layout()

# Mostrar la gráfica
#plt.show()
#.....................................

#.....................................
#total por rango de edades (a009)
#.....................................
# Cargar datos de los archivos CSV
archivo1 = "Listados CSV\\a009 2020.csv"
archivo2 = "Listados CSV\\a009 2021.csv"
archivo3 = "Listados CSV\\a009 2022.csv"
archivo4 = "Listados CSV\\a009 2023.csv"

# Cargar datos específicos de cada archivo para el primer grupo de barras (menor de 20 años)
datos1_1 = pd.read_csv(archivo1).iloc[0, 1]  # Selecciona la celda en la primera fila y segunda columna
datos2_1 = pd.read_csv(archivo2).iloc[0, 1]  # Selecciona la celda en la primera fila y segunda columna
datos3_1 = pd.read_csv(archivo3).iloc[0, 1]  # Selecciona la celda en la primera fila y segunda columna
datos4_1 = pd.read_csv(archivo4).iloc[0, 1]  # Selecciona la celda en la primera fila y segunda columna

# Cargar datos específicos de cada archivo para el segundo grupo de barras (20 a 29 años)
datos1_2 = pd.read_csv(archivo1).iloc[1, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos2_2 = pd.read_csv(archivo2).iloc[1, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos3_2 = pd.read_csv(archivo3).iloc[1, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos4_2 = pd.read_csv(archivo4).iloc[1, 1]  # Selecciona la celda en la segunda fila y segunda columna

# Cargar datos específicos de cada archivo para el tercer grupo de barras (30 a 39 años)
datos1_3 = pd.read_csv(archivo1).iloc[2, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos2_3 = pd.read_csv(archivo2).iloc[2, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos3_3 = pd.read_csv(archivo3).iloc[2, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos4_3 = pd.read_csv(archivo4).iloc[2, 1]  # Selecciona la celda en la segunda fila y segunda columna

# Cargar datos específicos de cada archivo para el cuarto grupo de barras (40 a 49 años)
datos1_4 = pd.read_csv(archivo1).iloc[3, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos2_4 = pd.read_csv(archivo2).iloc[3, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos3_4 = pd.read_csv(archivo3).iloc[3, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos4_4 = pd.read_csv(archivo4).iloc[3, 1]  # Selecciona la celda en la segunda fila y segunda columna

# Cargar datos específicos de cada archivo para el quinto grupo de barras (50 a 59 años)
datos1_5 = pd.read_csv(archivo1).iloc[4, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos2_5 = pd.read_csv(archivo2).iloc[4, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos3_5 = pd.read_csv(archivo3).iloc[4, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos4_5 = pd.read_csv(archivo4).iloc[4, 1]  # Selecciona la celda en la segunda fila y segunda columna

# Cargar datos específicos de cada archivo para el sexto grupo de barras (Mayor de 60 años)
datos1_6 = pd.read_csv(archivo1).iloc[5, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos2_6 = pd.read_csv(archivo2).iloc[5, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos3_6 = pd.read_csv(archivo3).iloc[5, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos4_6 = pd.read_csv(archivo4).iloc[5, 1]  # Selecciona la celda en la segunda fila y segunda columna


# Valores y etiquetas para las barras
valores_1 = [datos1_1, datos2_1, datos3_1, datos4_1]
valores_2 = [datos1_2, datos2_2, datos3_2, datos4_2]
valores_3 = [datos1_3, datos2_3, datos3_3, datos4_3]
valores_4 = [datos1_4, datos2_4, datos3_4, datos4_4]
valores_5 = [datos1_5, datos2_5, datos3_5, datos4_5]
valores_6 = [datos1_6, datos2_6, datos3_6, datos4_6]
archivos = ['2020', '2021', '2022', '2023']

colores_1 = ["#bf00bf", "#bf00bf", "#bf00bf", "#bf00bf"]
colores_2 = ["#bfbf00", "#bfbf00", "#bfbf00", "#bfbf00"]
colores_3 = ["#00ba38", "#00ba38", "#00ba38", "#00ba38"]
colores_4 = ["#ff0000", "#ff0000", "#ff0000", "#ff0000"]
colores_5 = ["#00bfbf", "#00bfbf", "#00bfbf", "#00bfbf"]
colores_6 = ["#008000", "#008000", "#008000", "#008000"]

# Ancho de las barras
ancho_barra = 0.1

# Desplazamiento en el eje x para separar los grupos de barras
desplazamiento_x = 0.3
desplazamiento_x1 = 0.2
desplazamiento_x2 = 0.1
desplazamiento_x3 = 0


# Crear la gráfica de barras para el primer grupo
group1 = plt.bar([i - desplazamiento_x for i in range(len(archivos))], valores_1, width=ancho_barra, color=colores_1, label='Menor 20 Años')

# Crear la gráfica de barras para el segundo grupo
group2 = plt.bar([i - desplazamiento_x1 for i in range(len(archivos))], valores_2, width=ancho_barra, color=colores_2, label='Desde 20 a 29 Años')

# Crear la gráfica de barras para el tercer grupo
group3 = plt.bar([i - desplazamiento_x2 for i in range(len(archivos))], valores_3, width=ancho_barra, color=colores_3, label='Desde 30 a 39 Años')

# Crear la gráfica de barras para el cuarto grupo
group4 = plt.bar([i - desplazamiento_x3 for i in range(len(archivos))], valores_4, width=ancho_barra, color=colores_4, label='Desde 40 a 49 Años')

# Crear la gráfica de barras para el quinto grupo
group5 = plt.bar([i + desplazamiento_x2 for i in range(len(archivos))], valores_5, width=ancho_barra, color=colores_5, label='Desde 50 a 59 Años')

# Crear la gráfica de barras para el sexto grupo
group6 = plt.bar([i + desplazamiento_x1 for i in range(len(archivos))], valores_6, width=ancho_barra, color=colores_6, label='Mayor de 60 Años')

# Añadir etiquetas y título
plt.xlabel('Año')
plt.ylabel('Cantidad de casos')
plt.title('Total de casos por rango de edades')

# Añadir leyenda
plt.legend()

# Ajustar el eje x para mostrar los años correctamente
plt.xticks(range(len(archivos)), archivos)

# Mostrar la gráfica
#plt.show()

#----------------------------------------- [ Casos de accidentes y enfermedades ] -----------------------------------------#

df1 = pd.read_csv("Listados CSV\\a001 2020.csv")    #Abrimos el archivo csv correspondiente a los casos del 2020
df2 = pd.read_csv("Listados CSV\\a001 2021.csv")    #Abrimos el archivo csv correspondiente a los casos del 2021
df3= pd.read_csv("Listados CSV\\a001 2022.csv")     #Abrimos el archivo csv correspondiente a los casos del 2022
df4 = pd.read_csv("Listados CSV\\a001 2023.csv")    #Abrimos el archivo csv correspondiente a los casos del 2023
to = [df1,df2,df3,df4]                              #Guardamos los archivos en una lista
anos = [2020,2021,2022,2023]                        #Predefinimos los años

lista_suma_accidentes,lista_suma_enfermedades = suma(to,"AT","EP")  #llamamos a la funcion

#----------------------------------------------- [ Generacion del Gráfico ] -----------------------------------------------#

plt.style.use("dark_background")                                                                        #Dandole un estilo oscuro al grafico
plt.figure(figsize=(10,6))                                                                              #Tamaño del grafico
plt.xlabel("Años")                                                                                      #Agregamos un label al eje X
plt.ylabel("Casos")                                                                                     #Agregamos un label al eje Y
plt.title("Reportes de accidentes vs enfermedeades 2020-2023")                                          #Agregamos un titulo a la grafica
plt.xticks([2020,2021,2022,2023])                                                                       #Configuramos para que se vean los años que nos interesan
plt.yticks(range(0,50000,2000))                                                                         #Configuramos para que se vean los años que nos interesan
plt.plot(anos,lista_suma_accidentes,marker = "o",linestyle = "--", color ="r",label="Accidentes")  
plt.plot(anos,lista_suma_enfermedades,marker = "o",linestyle = "--", color ="y",label="Enfermedades")
plt.style.use("default")                                                                                #Le damos otro estilo a la laeyenda
plt.legend(loc = 10)                                                                                    #Posicionamos la leyenda en el centro
#plt.show()                                                                                              #Mostramos el grafico
#--------------------------------------------------------- [  ] ----------------------------------------------------------#


#ocupaciones (a009)
#.....................................
# Cargar datos de los archivos CSV
archivo111 = "Listados CSV\\a012 2020.csv"
archivo222 = "Listados CSV\\a012 2021.csv"
archivo333 = "Listados CSV\\a012 2022.csv"
archivo444 = "Listados CSV\\a012 2023.csv"

# Cargar datos específicos de cada archivo para el primer grupo de barras (menor de 20 años)
datos1_111 = pd.read_csv(archivo111).iloc[0, 1]  # Selecciona la celda en la primera fila y segunda columna
datos2_111 = pd.read_csv(archivo222).iloc[0, 1]  # Selecciona la celda en la primera fila y segunda columna
datos3_111 = pd.read_csv(archivo333).iloc[0, 1]  # Selecciona la celda en la primera fila y segunda columna
datos4_111 = pd.read_csv(archivo444).iloc[0, 1]  # Selecciona la celda en la primera fila y segunda columna

# Cargar datos específicos de cada archivo para el segundo grupo de barras (20 a 29 años)
datos1_222 = pd.read_csv(archivo111).iloc[1, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos2_222 = pd.read_csv(archivo222).iloc[1, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos3_222 = pd.read_csv(archivo333).iloc[1, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos4_222 = pd.read_csv(archivo444).iloc[1, 1]  # Selecciona la celda en la segunda fila y segunda columna

# Cargar datos específicos de cada archivo para el tercer grupo de barras (30 a 39 años)
datos1_333 = pd.read_csv(archivo111).iloc[2, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos2_333 = pd.read_csv(archivo222).iloc[2, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos3_333 = pd.read_csv(archivo333).iloc[2, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos4_333 = pd.read_csv(archivo444).iloc[2, 1]  # Selecciona la celda en la segunda fila y segunda columna

# Cargar datos específicos de cada archivo para el cuarto grupo de barras (40 a 49 años)
datos1_444 = pd.read_csv(archivo111).iloc[3, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos2_444 = pd.read_csv(archivo222).iloc[3, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos3_444 = pd.read_csv(archivo333).iloc[3, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos4_444 = pd.read_csv(archivo444).iloc[3, 1]  # Selecciona la celda en la segunda fila y segunda columna

# Cargar datos específicos de cada archivo para el quinto grupo de barras (50 a 59 años)
datos1_555 = pd.read_csv(archivo111).iloc[4, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos2_555 = pd.read_csv(archivo222).iloc[4, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos3_555 = pd.read_csv(archivo333).iloc[4, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos4_555 = pd.read_csv(archivo444).iloc[4, 1]  # Selecciona la celda en la segunda fila y segunda columna

# Cargar datos específicos de cada archivo para el sexto grupo de barras (Mayor de 60 años)
datos1_666 = pd.read_csv(archivo111).iloc[5, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos2_666 = pd.read_csv(archivo222).iloc[5, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos3_666 = pd.read_csv(archivo333).iloc[5, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos4_666 = pd.read_csv(archivo444).iloc[5, 1]  # Selecciona la celda en la segunda fila y segunda columna

# Cargar datos específicos de cada archivo para el sexto grupo de barras (Mayor de 60 años)
datos1_777 = pd.read_csv(archivo111).iloc[6, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos2_777 = pd.read_csv(archivo222).iloc[6, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos3_777 = pd.read_csv(archivo333).iloc[6, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos4_777 = pd.read_csv(archivo444).iloc[6, 1]  # Selecciona la celda en la segunda fila y segunda columna

# Cargar datos específicos de cada archivo para el sexto grupo de barras (Mayor de 60 años)
datos1_888 = pd.read_csv(archivo111).iloc[7, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos2_888 = pd.read_csv(archivo222).iloc[7, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos3_888 = pd.read_csv(archivo333).iloc[7, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos4_888 = pd.read_csv(archivo444).iloc[7, 1]  # Selecciona la celda en la segunda fila y segunda columna

# Cargar datos específicos de cada archivo para el sexto grupo de barras (Mayor de 60 años)
datos1_999 = pd.read_csv(archivo111).iloc[8, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos2_999 = pd.read_csv(archivo222).iloc[8, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos3_999 = pd.read_csv(archivo333).iloc[8, 1]  # Selecciona la celda en la segunda fila y segunda columna
datos4_999 = pd.read_csv(archivo444).iloc[8, 1]  # Selecciona la celda en la segunda fila y segunda columna



# Valores y etiquetas para las barras
valores_111 = [datos1_111, datos2_111, datos3_111, datos4_111]
valores_222 = [datos1_222, datos2_222, datos3_222, datos4_222]
valores_333 = [datos1_333, datos2_333, datos3_333, datos4_333]
valores_444 = [datos1_444, datos2_444, datos3_444, datos4_444]
valores_555 = [datos1_555, datos2_555, datos3_555, datos4_555]
valores_666 = [datos1_666, datos2_666, datos3_666, datos4_666]
valores_777 = [datos1_777, datos2_777, datos3_777, datos4_777]
valores_888 = [datos1_888, datos2_888, datos3_888, datos4_888]
valores_999 = [datos1_999, datos2_999, datos3_999, datos4_999]
archivoss = ['2020', '2021', '2022', '2023']

colores_11 = ["#bf00bf", "#bf00bf", "#bf00bf", "#bf00bf"]
colores_22 = ["#bfbf00", "#bfbf00", "#bfbf00", "#bfbf00"]
colores_33 = ["#00ba38", "#00ba38", "#00ba38", "#00ba38"]
colores_44 = ["#ff0000", "#ff0000", "#ff0000", "#ff0000"]
colores_55 = ["#00bfbf", "#00bfbf", "#00bfbf", "#00bfbf"]
colores_66 = ["#008000", "#008000", "#008000", "#008000"]
colores_77 = ["#800080", "#800080", "#800080", "#800080"]
colores_88 = ["#FFA500", "#FFA500", "#FFA500", "#FFA500"]
colores_99 = ["#9932CC", "#9932CC", "#9932CC", "#9932CC"]

# Ancho de las barras
ancho_barra = 0.1

# Desplazamiento en el eje x para separar los grupos de barras
desplazamiento_xx = 0.3
desplazamiento_x11 = 0.2
desplazamiento_x22 = 0.1
desplazamiento_x33 = 0

plt.figure(figsize=(20,20))  
# Crear la gráfica de barras para el primer grupo
group11 = plt.bar([i - desplazamiento_xx for i in range(len(archivoss))], valores_111, width=ancho_barra, color=colores_11, label='AGRICULTORES Y TRABAJADORES CALIFICADOS AGROPECUARIOS Y PESQUEROS')

# Crear la gráfica de barras para el segundo grupo
group22 = plt.bar([i - desplazamiento_x11 for i in range(len(archivoss))], valores_222, width=ancho_barra, color=colores_22, label='EMPLEADOS DE OFICINA')

# Crear la gráfica de barras para el tercer grupo
group33 = plt.bar([i - desplazamiento_x22 for i in range(len(archivoss))], valores_333, width=ancho_barra, color=colores_33, label='FUERZAS ARMADAS')

# Crear la gráfica de barras para el cuarto grupo
group44 = plt.bar([i - desplazamiento_x33 for i in range(len(archivoss))], valores_444, width=ancho_barra, color=colores_44, label='OFICIALES, OPERARIOS Y ARTESANOS DE ARTES MECANICAS Y DE OTROS OFICIOS')

# Crear la gráfica de barras para el quinto grupo
group55 = plt.bar([i + desplazamiento_x22 for i in range(len(archivoss))], valores_555, width=ancho_barra, color=colores_55, label='OPERADORES DE INSTALACIONES Y MAQUINAS Y MONTADORES')

# Crear la gráfica de barras para el sexto grupo
group66 = plt.bar([i + desplazamiento_x11 for i in range(len(archivoss))], valores_666, width=ancho_barra, color=colores_66, label='PROFESIONALES CIENTIFICOS E INTELECTUALES')

group77 = plt.bar([i + desplazamiento_xx for i in range(len(archivoss))], valores_777, width=ancho_barra, color=colores_77, label='TECNICOS Y PROFESIONALES DE NIVEL MEDIO')

group88 = plt.bar([i + desplazamiento_x11 for i in range(len(archivoss))], valores_888, width=ancho_barra, color=colores_88, label='TRABAJADORES DE LOS SERVICIOS Y VENDEDORES DE COMERCIOS Y MERCADOS')

group99 = plt.bar([i + desplazamiento_x22 for i in range(len(archivoss))], valores_999, width=ancho_barra, color=colores_99, label='TRABAJADORES NO CALIFICADOS')


# Añadir etiquetas y título                                                                            #Tamaño del grafico
plt.xlabel('Año')
plt.ylabel('Cantidad de casos')
plt.title('Total de casos por Grupo de ocupacion')

# Añadir leyenda
plt.legend(loc=2)

# Ajustar el eje x para mostrar los años correctamente
plt.xticks(range(len(archivoss)), archivoss)

# Mostrar la gráfica
#plt.show()
"""