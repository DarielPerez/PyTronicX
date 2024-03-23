
import pandas as pd
import matplotlib.pyplot as plt

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
plt.show()
