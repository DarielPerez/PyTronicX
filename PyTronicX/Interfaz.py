import pandas as pd
import csv
import matplotlib.pyplot as plt
import tkinter as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
font_titule = ("Verdana", 16, "bold")
font_text = ("Verdana", 12,)
# la ruta original del archivo



# lectura de datos
datos = pd.read_csv("Listados CSV\\Partes del cuerpo.csv")

# filtro
datos_declinados = datos[datos['Estado'] == 'declinado']

datos_calificados = datos[datos['Estado'] == 'calificado']

datos_proceso_calificacion = datos[datos['Estado'] == 'proceso de calificacion']

# decido donde la voy a guardar

ruta_csv_declinados = "Listados CSV\declinado.csv"


ruta_csv_calificados = "Listados CSV\calificado.csv"

ruta_csv_proceso_calificacion = "Listados CSV\proceso_calificacion.csv"

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



def grafica_out(n_grafica, size):
    global canvas
    if canvas == None:
        canvas = FigureCanvasTkAgg(n_grafica, master=grafica_label)    
    else:
        canvas.get_tk_widget().pack_forget()
        canvas = FigureCanvasTkAgg(n_grafica, master=grafica_label)    
        canvas.get_tk_widget().configure(width=1000, height=400) if not size else canvas.get_tk_widget().configure(width=1400, height=600)
        canvas.get_tk_widget().pack()

def grafica_1():
    grafica1, ax = plt.subplots(figsize=(25, 10))
    ax = plt.subplot()
    ax.hist(datos_calificados['Fecha_Reg_calific'], bins=50, color='green', alpha=0.7)
    ax.set_title('Vista general de los Datos Calificados')
    ax.set_xlabel('Etiqueta del eje X', fontsize=10)
    ax.set_ylabel('Etiqueta del eje Y', fontsize=10)
    plt.subplots_adjust(bottom=0.1, top=0.9)
    ax.grid(True)
    return grafica_out(grafica1, 0)



def grafica_2():
    grafica2, ax = plt.subplots(figsize=(25, 10))
    ax = plt.subplot()
    ax.hist(datos_declinados['Fecha_Reg_calific'], bins=50, color='red', alpha=0.7)
    ax.set_title('Vista general de los Datos Declinados')
    ax.set_xlabel('Etiqueta del eje X', fontsize=10)
    ax.set_ylabel('Etiqueta del eje Y', fontsize=10)
    plt.subplots_adjust(bottom=0.1, top=0.9)
    ax.grid(True)
    return grafica_out(grafica2, 0)


def grafica_3():
    num_calificados = datos[datos['Estado'] == 'calificado'].shape[0]
    num_declinado = datos[datos['Estado'] == 'declinado'].shape[0]
    # Etiquetas para las barras
    categorias = ['Calificados', 'Declinado']
    alturas = [num_calificados, num_declinado]
    colores = ['blue', 'red']
    grafica3, ax = plt.subplots(figsize=(25, 10))
    ax.bar(categorias, alturas, color=colores)
    ax.set_title('Comparación de Calificados y Declinados')
    ax.set_xlabel('Estado')
    ax.set_ylabel('Número de casos')
    plt.subplots_adjust(bottom=0.1, top=0.9)
    ax.grid(True)
    return grafica_out(grafica3, 0)


def grafica_4():
    columna_interes = 'Parte_Lesion'
    # Contar la frecuencia de cada segmento en la columna de interés
    frecuencia_segmentos = datos_calificados[columna_interes].value_counts()

    segmentos_mas_comunes = frecuencia_segmentos.head(20)

    grafica4, ax = plt.subplots(figsize=(15, 10))

    ax.barh(segmentos_mas_comunes.index, segmentos_mas_comunes, color='skyblue')

    ax.set_title('20 lesiones más frecuentes de los datos calificados ({})'.format(columna_interes))
    ax.set_xlabel('Segmento')
    ax.set_ylabel('Frecuencia')
    plt.yticks(rotation=45)

    plt.tight_layout()
    return grafica_out(grafica4, 1)

def grafica_5():
    columna_interes = 'Parte_Lesion'
    # Contar la frecuencia de cada segmento en la columna de interés
    frecuencia_segmentos = datos_declinados[columna_interes].value_counts()

    segmentos_mas_comunes = frecuencia_segmentos.head(20)

    grafica5, ax = plt.subplots(figsize=(15, 10))

    ax.barh(segmentos_mas_comunes.index, segmentos_mas_comunes, color='red')

    ax.set_title('20 lesiones más frecuentes de los datos declinados ({})'.format(columna_interes))
    ax.set_xlabel('Segmento')
    ax.set_ylabel('Frecuencia')
    plt.yticks(rotation=45)

    plt.tight_layout()
    return grafica_out(grafica5, 1)

def grafica_6():
    grafica6, ax = plt.subplots(figsize=(25, 10))
    ax.hist(datos_proceso_calificacion['Parte_Lesion'], bins=50, color='blue', alpha=0.7)
    ax.set_title('Datos de proceso de calificación')
    ax.set_xlabel('Etiqueta del eje X', fontsize=10)
    ax.set_ylabel('Etiqueta del eje Y', fontsize=10)
    plt.grid(True)
    return grafica_out(grafica6, 0)


# Crear ventana principal
window_principal = ttk.Tk()
window_principal.title(string="Ventana de Gráficas")
window_principal.geometry('800x600')
window_principal.iconbitmap("python.ico")
#window.maxsize(width=1000, height=800)

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

