import pandas as pd
import csv
import matplotlib.pyplot as plt
import tkinter as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
font_titule = ("Verdana", 16, "bold")
font_text = ("Verdana", 12,)

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
def grafica_out(n_grafica, size):
    global canvas
    if canvas == None:
        canvas = FigureCanvasTkAgg(n_grafica, master=grafica_label)    
    else:
        canvas.get_tk_widget().pack_forget()
        canvas = FigureCanvasTkAgg(n_grafica, master=grafica_label)    
        canvas.get_tk_widget().configure(width=1000, height=400) if not size else canvas.get_tk_widget().configure(width=1400, height=600)
        canvas.get_tk_widget().pack()

# Convertir la columna de fechas a formato de fecha
datos_calificados['Fecha_Reg_calific'] = pd.to_datetime(datos_calificados['Fecha_Reg_calific'])

# Crear una nueva columna con el mes y año como cadena de texto
datos_calificados['Mes_Año'] = datos_calificados['Fecha_Reg_calific'].dt.to_period('M').astype(str)

# Agrupar los datos por mes y año y contar la cantidad de datos en cada grupo
datos_agrupados = datos_calificados.groupby('Mes_Año').size().reset_index(name='Cantidad')

#creacion de graficos de barra de los datos calificados por mes del año
def grafica_1():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax = plt.subplot()
    ax.set_title('Cantidad de datos calificados por mes y año')
    ax.set_xlabel('Mes y Año', fontsize=10)
    ax.set_ylabel('Cantidad', fontsize=10)
    ax.set_xticks(rotation=45, ha='right')
    ax.grid(True)
    return grafica_out(fig, 0)




# Convertir la columna de fechas a formato de fecha
datos_declinados['Fecha_Reg_calific'] = pd.to_datetime(datos_declinados['Fecha_Reg_calific'])

# Crear una nueva columna con el mes y año como cadena de texto
datos_declinados['Mes_Año'] = datos_declinados['Fecha_Reg_calific'].dt.to_period('M').astype(str)

# Agrupar los datos por mes y año y contar la cantidad de datos en cada grupo
datos_agrupados = datos_declinados.groupby('Mes_Año').size().reset_index(name='Cantidad')

# Crear el gráfico de barras
def grafica_2():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax = plt.subplot()
    ax.bar(datos_agrupados['Mes_Año'], datos_agrupados['Cantidad'], color='red', alpha=0.7)
    ax.set_title('Cantidad de datos Declinados por mes y año')
    ax.set_xlabel('Mes y Año', fontsize=10)
    ax.set_ylabel('Cantidad', fontsize=10)
    ax.set_xticks(rotation=45, ha='right')
    ax.grid(True)
    return grafica_out(fig, 0)



# Contar el número de filas calificadas y declinadas
#esto lo toma de los datos generales
datos = pd.read_csv("Partes del cuerpo.csv")
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
plt.show() 


#parte lesion

columna_interes = 'Parte_Lesion'

# Contar la frecuencia de cada segmento en la columna de interés
frecuencia_segmentos = datos_calificados[columna_interes].value_counts()
segmentos_mas_comunes = frecuencia_segmentos.head(20)

# Graficar 
def grafica_4():
    fig, ax = plt.subplots(figsize=(22, 10))
    segmentos_mas_comunes.plot(kind='barh', color='skyblue', ax=ax)
    ax.set_title('20 lesiones mas frecuentes de los datos calificados'.format(columna_interes))
    ax.set_xlabel('Frecuencia')
    ax.set_ylabel('Partes del cuerpo')
    ax.set_xticks(rotation=0)
    plt.tight_layout()
    return grafica_out(fig, 0)


    #lo mismo pero con los datos declinados
    frecuencia_segmentos = datos_declinados[columna_interes].value_counts()
    segmentos_mas_comunes = frecuencia_segmentos.head(20)

def grafica_5():
    fig, ax = plt.subplots(figsize=(22, 10))
    segmentos_mas_comunes.plot(kind='barh', color='skyblue', ax=ax)
    ax.set_title('20 lesiones mas frecuentes de los datos declinados'.format(columna_interes))
    ax.set_xlabel('Frecuencia')
    ax.set_ylabel('Partes del cuerpo')
    ax.set_xticks(rotation=0)
    plt.tight_layout()
    return grafica_out(fig, 0)


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

def grafica_6():
    fig, ax = plt.subplots(figsize=(10, 6))
    # Graficar empresas públicas
    ax.plot(years, public_cases, color='blue', label='Empresas Públicas', marker='o')
    # Graficar empresas privadas
    ax.plot(years, private_cases, color='red', label='Empresas Privadas', marker='x')
    # Etiquetas y título
    ax.set_xlabel('Año')
    ax.set_ylabel('Casos')
    ax.set_title('Total de casos por tipo de empresas (a010) por año')
    # Mostrar todos los años en el eje x
    ax.set_xticks(years)
    # Leyenda
    ax.legend()
    # Cuadrícula
    ax.grid(True)
    return grafica_out(fig, 0)



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

def grafica_7():
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
    return grafica_out(fig, 0)


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

def grafica_8():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Posiciones de las barras
    desplazamientos = [-0.25, 0, 0.25, 0.5, -0.5, 0]

    # Crear las gráficas de barras
    barras = []
    colores = [colores_1, colores_2, colores_3, colores_4, colores_5, colores_6]
    etiquetas = ['Menor 20 Años', 'Desde 20 a 29 Años', 'Desde 30 a 39 Años', 'Desde 40 a 49 Años', 'Desde 50 a 59 Años', 'Mayor de 60 Años']
    for i in range(len(valores_1)):
        barras.append(ax.bar(i + desplazamientos[i], [valores_1[i], valores_2[i], valores_3[i], valores_4[i], valores_5[i], valores_6[i]], 
                            width=ancho_barra, color=colores[i], label=etiquetas[i]))

    # Añadir etiquetas y título
    ax.set_xlabel('Año')
    ax.set_ylabel('Cantidad de casos')
    ax.set_title('Total de casos por rango de edades')

    # Añadir leyenda
    ax.legend(handles=barras, labels=etiquetas)

    # Ajustar el eje x para mostrar los años correctamente
    ax.set_xticks(range(len(archivos)), archivos)
    return grafica_out(fig, 0)

#----------------------------------------- [ Casos de accidentes y enfermedades ] -----------------------------------------#

df1 = pd.read_csv("Listados CSV\\a001 2020.csv")    #Abrimos el archivo csv correspondiente a los casos del 2020
df2 = pd.read_csv("Listados CSV\\a001 2021.csv")    #Abrimos el archivo csv correspondiente a los casos del 2021
df3= pd.read_csv("Listados CSV\\a001 2022.csv")     #Abrimos el archivo csv correspondiente a los casos del 2022
df4 = pd.read_csv("Listados CSV\\a001 2023.csv")    #Abrimos el archivo csv correspondiente a los casos del 2023
to = [df1,df2,df3,df4]                              #Guardamos los archivos en una lista
anos = [2020,2021,2022,2023]                        #Predefinimos los años

lista_suma_accidentes,lista_suma_enfermedades = suma(to,"AT","EP")  #llamamos a la funcion

#----------------------------------------------- [ Generacion del Gráfico ] -----------------------------------------------#

def grafica_9():
    fig, ax = plt.subplots(figsize=(10, 6))
    # Damos estilo oscuro al subplot
    ax.set_facecolor('#212946')
    # Añadimos título
    ax.set_title('Reportes de accidentes vs enfermedades 2020-2023', color='white')
    # Etiquetas
    ax.set_xlabel('Años', color='white')
    ax.set_ylabel('Casos', color='white')
    # Configuramos las marcas en el eje X
    ax.set_xticks([2020, 2021, 2022, 2023])
    # Configuramos las marcas en el eje Y
    ax.set_yticks(range(0, 50000, 2000))

    # Línea de accidentes
    ax.plot(anos, lista_suma_accidentes, marker='o', linestyle='--', color='r', label='Accidentes')

    # Línea de enfermedades
    ax.plot(anos, lista_suma_enfermedades, marker='o', linestyle='--', color='y', label='Enfermedades')

    # Cambiamos el estilo de la leyenda
    plt.style.use('default')

    # Añadimos la leyenda
    ax.legend(loc=10, facecolor='#212946')
    #Posicionamos la leyenda en el centro
    return grafica_out(fig, 0)
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

def grafica_9():
# Ancho de las barras
    ancho_barra = 0.1

    # Desplazamiento en el eje x para separar los grupos de barras
    desplazamiento_x = [0.3, 0.2, 0.1, 0, -0.1, -0.2, -0.3]

    # Etiquetas de los grupos
    grupos = ['AGRICULTORES Y TRABAJADORES CALIFICADOS AGROPECUARIOS Y PESQUEROS',
            'EMPLEADOS DE OFICINA',
            'FUERZAS ARMADAS',
            'OFICIALES, OPERARIOS Y ARTESANOS DE ARTES MECANICAS Y DE OTROS OFICIOS',
            'OPERADORES DE INSTALACIONES Y MAQUINAS Y MONTADORES',
            'PROFESIONALES CIENTIFICOS E INTELECTUALES',
            'TECNICOS Y PROFESIONALES DE NIVEL MEDIO',
            'TRABAJADORES DE LOS SERVICIOS Y VENDEDORES DE COMERCIOS Y MERCADOS',
            'TRABAJADORES NO CALIFICADOS']

    # Colores para cada grupo
    colores = ['#008000', '#0000FF', '#FF0000', '#800080', '#FFFF00', '#00FFFF', '#808080', '#FF8000', '#C0C0C0']

    # Crear la figura y los subplots
    fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(20, 20))

    # Recorrer los subplots y crear las gráficas de barras
    for i, ax in enumerate(axs.flatten()):
        # Obtener los valores para el grupo actual
        valores = eval(f"valores_{i+1}11")

        # Crear la gráfica de barras
        ax.bar([i - desplazamiento_x[i] for i in range(len(archivoss))], valores, width=ancho_barra, color=colores[i], label=grupos[i])

        # Ajustar el eje x para mostrar los años correctamente
        ax.set_xticks(range(len(archivoss)), archivoss)

        # Eliminar las etiquetas del eje y si no es el subplot inferior
        if i < 6:
            ax.set_xlabel('')
        if i % 3 != 0:
            ax.set_ylabel('')

    # Agregar título general
    fig.suptitle('Total de casos por Grupo de ocupacion')

    # Agregar leyenda
    handles, labels = axs[2, 2].get_legend_handles_labels()
    fig.legend(handles, labels, loc='center right')
    return grafica_out(fig, 0)



# Crear ventana principal
window_principal = ttk.Tk()
window_principal.title(string="Ventana de Gráficas")
window_principal.configure(background="light blue")
window_principal.geometry('800x600')
window_principal.iconbitmap("python.ico")

#Creación de los menus

barra_menus = ttk.Menu(window_principal)
window_principal.config(menu=barra_menus)


# creamos un menú cuyo contenedor será la barra de menús
menu = ttk.Menu(barra_menus, tearoff=False)

# añadimos opciones al menú indicando su nombre y acción asociado
menu.add_command(label='Gráfica 1', command=grafica_1)
menu.add_command(label='Gráfica 2', command=grafica_2)
menu.add_command(label='Gráfica 3', command=grafica_3)
menu.add_command(label='Gráfica 4', command=grafica_4)
menu.add_command(label='Gráfica 5', command=grafica_5)
menu.add_command(label='Gráfica 6', command=grafica_6)
menu.add_command(label='Gráfica 4', command=grafica_7)
menu.add_command(label='Gráfica 5', command=grafica_8)
menu.add_command(label='Gráfica 6', command=grafica_9)

# añadimos una línea separadora y la opción de salir
menu.add_separator()
menu.add_command(label='Salir', command=window_principal.destroy)

# finalmente añadimos el menú a la barra de menús
barra_menus.add_cascade(label="Menú", menu=menu)


# Obtener la ruta local del archivo
texto = ttk.Label(window_principal, text="Bienvenidos a nuestra interfaz de gráficas.\nPuedes indagar en nuestro menú para ver las gáficas.",
    font=font_text,
    padx=20,
    pady=15,
    background="SeaGreen1",
    compound="top",
    anchor="center",
    justify="left",
    borderwidth=2,
    relief="groove")

texto.place(y=5, x=200)
grafica_label = ttk.Label(window_principal)
grafica_label.place(x=50, y=75)
canvas = None
window_principal.mainloop()