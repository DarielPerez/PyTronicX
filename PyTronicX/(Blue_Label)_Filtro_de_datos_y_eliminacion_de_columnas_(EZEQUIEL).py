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
        df[i] = df[i].dropna()                      # Eliminamos los datos nulos
        cache_accidente.append(df[i][x].sum())      #Sumamos la columna de los accidentes y lo guardamos en los datos cache
        cache_enfermedades.append(df[i][z].sum())   #Sumamos la columna de las enfermedades y lo guardamos en los datos cache
    return cache_accidente,cache_enfermedades       #Retornamos las listas caches

# la ruta original del archivo
ruta_csv_original = "Listados CSV\Partes del cuerpo.csv"

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
        canvas.get_tk_widget().configure(width=1000, height=400) if not size else canvas.get_tk_widget().configure(width=1500, height=700)
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
    ax.bar(datos_agrupados['Mes_Año'], datos_agrupados['Cantidad'], color='blue', alpha=0.7)
    ax.set_title('Cantidad de datos calificados por mes y año')
    ax.set_xlabel('Mes y Año', fontsize=10)
    ax.set_ylabel('Cantidad', fontsize=10)
    #ax.set_xticks(rotation=45)
    ax.grid(True)
    texto.configure(text="Gráfica 1: Cantidad de Datos Calificados Por Año y Mes.")
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
    #ax.set_xticks(rotation=45, ha='right')
    ax.grid(True)
    texto.configure(text="Gráfica 2: Cantidad de Datos Declinados Por Año y Mes")
    return grafica_out(fig, 0)

# Contar el número de filas calificadas y declinadas
#esto lo toma de los datos generales
datos = pd.read_csv("Listados CSV/Partes del cuerpo.csv")
num_calificados = datos[datos['Estado'] == 'calificado'].shape[0]
num_declinado = datos[datos['Estado'] == 'declinado'].shape[0]
categorias = ['Calificados', 'Declinados']
explode = [0, 0.1]
alturas = [num_calificados, num_declinado]
colores = ['limegreen', 'red']

def grafica_3():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(alturas, labels=categorias, colors=colores, autopct='%1.1f%%', 
            startangle=140, wedgeprops = {"linewidth": 1, "edgecolor": "white"}, explode = explode)
    ax.axis('equal')
    ax.set_title('Comparación de Calificados y Declinados')
    texto.configure(text="Gráfica 3: Comparación entre datos Calificados y Declinados")
    return grafica_out(fig, 0)

#parte lesion
columna_interes = 'Parte_Lesion'
# Contar la frecuencia de cada segmento en la columna de interés
frecuencia_segmentos = datos_calificados[columna_interes].value_counts()
lista_indice = frecuencia_segmentos.head(20).index.tolist()
valores = frecuencia_segmentos.head(20).tolist()
indice = [str(i+1) for i in range(len(lista_indice))]


# Graficar 
def grafica_4():
    # Graficar 
    fig, ax = plt.subplots(figsize=(18, 8))
    indice_lesion = list(map(lambda x : 'Lesion '+ x, indice))
    ax.barh(indice_lesion, valores, label=lista_indice)
    ax.set_title('20 lesiones mas frecuentes de los datos calificados')  # Título del gráfico
    ax.set_xlabel('Frecuencia')  # Etiqueta del eje x
    ax.set_ylabel('Partes del cuerpo')  # Etiqueta del eje y
    leyenda = list(map(lambda x : f'{x[0]} == {x[1]}',zip(indice, lista_indice)))
    ax.legend(leyenda, loc='upper right', fontsize='10', title='Leyenda', title_fontsize='12', shadow=0, borderpad=1, labelspacing=0.1, frameon=True, edgecolor='black', ncol=1)
    plt.tight_layout()
    texto.configure(text="Gráfica 4: 20 lesiones más frecuentes Calificados")
    return grafica_out(fig, 1)




def grafica_5():
    columna_interes = 'Parte_Lesion'
    frecuencia_segmentos = datos_declinados[columna_interes].value_counts()
    lista_indice = frecuencia_segmentos.head(20).index.tolist()
    valores = frecuencia_segmentos.head(20).tolist()
    indice = [str(i+1) for i in range(len(lista_indice))]
    # Graficar 
    fig, ax = plt.subplots(figsize=(40, 15))
    indice_lesion = list(map(lambda x : 'Lesion '+ x, indice))
    ax.barh(indice_lesion, valores, label=lista_indice, color='red')
    ax.set_title('20 lesiones mas frecuentes de los datos declinados')  # Título del gráfico
    ax.set_xlabel('Frecuencia')  # Etiqueta del eje x
    ax.set_ylabel('Partes del cuerpo')  # Etiqueta del eje y
    leyenda = list(map(lambda x : f'{x[0]} == {x[1]}',zip(indice, lista_indice)))
    ax.legend(leyenda, loc='upper right', fontsize='10', title='Leyenda', title_fontsize='12', shadow=0, borderpad=1, labelspacing=0.1, frameon=True, edgecolor='black', ncol=1)
    plt.tight_layout()
    texto.configure(text="Gráfica 5: 20 lesiones más frecuentes Declinadas")
    return grafica_out(fig, 1)

    
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
    texto.configure(text="Gráfica 6: Total de casos por tipo de empresas")
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
    texto.configure(text="Gráfica 7: Total de casos por Genero")
    return grafica_out(fig, 0)

#.....................................
#total por rango de edades (a009)
#.....................................
# Cargar datos de los archivos CSV

#.....................................
#total por rango de edades (a009)
#.....................................
# Cargar datos de los archivos CSV
archivos_8 = ["Listados CSV\\a009 2020.csv",
            "Listados CSV\\a009 2021.csv", 
            "Listados CSV\\a009 2022.csv", 
            "Listados CSV\\a009 2023.csv"]


a = pd.read_csv(archivos_8[0])
datos_por_grupo_8 = [[] for _ in range(6)]
leyenda = [a.iloc[i,0] for i in range(len(a)-1)]

# Cargar datos de cada archivo CSV
for archivo in archivos_8:
    datos = pd.read_csv(archivo)
    cantidad = len(datos)-1
    for i in range(cantidad):  # Hay 10 grupos en total
        datos_por_grupo_8[i].append(datos.iloc[i, 1])


def grafica_8():
    # Ancho de las barras
    ancho_barra = 0.1

    # Desplazamiento en el eje x para separar los grupos de barras
    desplazamiento_xx = 0.3

    # Valores y etiquetas para las barras
    archivoss = ['2020', '2021', '2022', '2023']

    colores = ["#bf00bf", "#bfbf00", "#00ba38", "#ff0000", "#00bfbf", "#008000", "#FFA500"] # Ancho de las barras
    fig, ax = plt.subplots(figsize=(10, 6))  # Crear objeto de figura y subplot

    # Crear las barras para cada grupo
    for i in range(len(datos_por_grupo_8)):
        ax.bar([j + i * ancho_barra + desplazamiento_xx for j in range(len(archivoss))],
            datos_por_grupo[i],
            width=ancho_barra,
            color=colores[i],
            label=leyenda[i])
    # Añadir etiquetas y título
    ax.set_xlabel('Año')
    ax.set_ylabel('Cantidad de casos')
    ax.set_title('Total de casos por rango de edades')

    # Ajustar el eje x para mostrar los años correctamente
    ax.set_xticks([j + (len(archivoss) * ancho_barra + desplazamiento_xx) / 2 for j in range(len(archivoss))])
    ax.set_xticklabels(archivoss)

    # Mostrar la leyenda
    ax.legend(loc='upper left', fontsize='6', title='Leyenda', title_fontsize='8', shadow=0, borderpad=1, labelspacing=0.4, frameon=True, edgecolor='black', ncol=1)
    texto.configure(text="Gráfica 8: Total de casos por rango de edades")
    return grafica_out(fig, 0)


#----------------------------------------------- [ Generacion del Gráfico ] -----------------------------------------------#
#----------------------------------------- [ Casos de accidentes y enfermedades ] -----------------------------------------#

df1 = pd.read_csv("Listados CSV\\a001 2020.csv")    #Abrimos el archivo csv correspondiente a los casos del 2020
df2 = pd.read_csv("Listados CSV\\a001 2021.csv")    #Abrimos el archivo csv correspondiente a los casos del 2021
df3= pd.read_csv("Listados CSV\\a001 2022.csv")     #Abrimos el archivo csv correspondiente a los casos del 2022
df4 = pd.read_csv("Listados CSV\\a001 2023.csv")    #Abrimos el archivo csv correspondiente a los casos del 2023
to = [df1,df2,df3,df4]                              #Guardamos los archivos en una lista
anos = [2020,2021,2022,2023]                        #Predefinimos los años

lista_suma_accidentes,lista_suma_enfermedades = suma(to,"AT","EP")  #llamamos a la funcion
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
    texto.configure(text="Gráfica 9: Reporte de accidentes vs enfermedades 2020-2023")
    return grafica_out(fig, 0)
#--------------------------------------------------------- [  ] ----------------------------------------------------------#


archivos = ["Listados CSV\\a012 2020.csv",
            "Listados CSV\\a012 2021.csv",
            "Listados CSV\\a012 2022.csv",
            "Listados CSV\\a012 2023.csv"]
# Inicializar listas para almacenar datos
datos_por_grupo = [[] for _ in range(9)]
a = pd.read_csv(archivos[0])
leyenda = [a.iloc[i,0] for i in range(len(a)-1)]
# Cargar datos de cada archivo CSV
for archivo in archivos:
    datos = pd.read_csv(archivo)
    cantidad = len(datos)-1
    for i in range(cantidad):  # Hay 10 grupos en total
        datos_por_grupo[i].append(datos.iloc[i, 1])

# Ancho de las barras
ancho_barra = 0.1

# Desplazamiento en el eje x para separar los grupos de barras
desplazamiento_xx = 0.3

# Valores y etiquetas para las barras
archivoss = ['2020', '2021', '2022', '2023']

colores = ["#bf00bf", "#bfbf00", "#00ba38", "#ff0000", "#00bfbf", "#008000", "#800080", "#FFA500", "#9932CC"]

def grafica_10():
    fig, ax = plt.subplots(figsize=(10, 6))  # Crear objeto de figura y subplot

    # Crear las barras para cada grupo

    for i in range(len(datos_por_grupo)):
        ax.bar([j + i * ancho_barra + desplazamiento_xx for j in range(len(archivoss))],
            datos_por_grupo[i],
            width=ancho_barra,
            color=colores[i],
            label=leyenda[i])
    # Añadir etiquetas y título
    ax.set_xlabel('Año')
    ax.set_ylabel('Cantidad de casos')
    ax.set_title('Total de casos por Grupo de ocupacion')

    # Ajustar el eje x para mostrar los años correctamente
    ax.set_xticks([j + (len(archivoss) * ancho_barra + desplazamiento_xx) / 2 for j in range(len(archivoss))])
    ax.set_xticklabels(archivoss)

    # Mostrar la leyenda
    ax.legend(loc='upper left', fontsize='4', title='Leyenda', title_fontsize='6', shadow=0, borderpad=1, labelspacing=0.4, frameon=True, edgecolor='black', ncol=1)
    texto.configure(text="Gráfica 10: Total de casos por grupo de ocupacion")
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
menu.add_command(label='Gráfica 1: Cantidad de Datos Calificados Por Año y Mes', command=grafica_1)
menu.add_command(label='Gráfica 2: Cantidad de Datos Declinados Por Año y Mes', command=grafica_2)
menu.add_command(label='Gráfica 3: Comparación entre datos Calificados y Declinados', command=grafica_3)
menu.add_command(label='Gráfica 4: 20 lesiones más frecuentes Calificados', command=grafica_4)
menu.add_command(label='Gráfica 5: 20 lesiones más frecuentes Declinadas', command=grafica_5)
menu.add_command(label='Gráfica 6: Total de casos por tipo de empresas', command=grafica_6)
menu.add_command(label='Gráfica 7: Total de casos por Genero', command=grafica_7)
menu.add_command(label='Gráfica 8: Total de casos por rango de edades', command=grafica_8)
menu.add_command(label='Gráfica 9: Reporte de accidentes vs enfermedades 2020-2023', command=grafica_9)
menu.add_command(label='Gráfica 10: Total de casos por grupo de ocupacion', command=grafica_10)

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