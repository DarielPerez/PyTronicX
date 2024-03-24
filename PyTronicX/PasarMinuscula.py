import pandas as pd

def convertir_columna_a_minusculas(archivo_entrada, columna, archivo_salida):
    # Leer el archivo CSV
    datos = pd.read_csv(archivo_entrada)

    # Convertir la columna especificada a minúsculas
    datos[columna] = datos[columna].str.lower()

    # Guardar el archivo modificado
    datos.to_csv(archivo_salida, index=False, encoding='utf-8-sig')

# Ejemplo de uso
archivo_entrada = "Listados CSV\\Partes del cuerpo.csv"
columna_a_modificar = "Parte_Lesion"  # Reemplaza "Nombre" por el nombre de tu columna
archivo_salida = "Listados CSV\\Partes del cuerpo.csv"

convertir_columna_a_minusculas(archivo_entrada, columna_a_modificar, archivo_salida)