import matplotlib.pyplot as plt

'''
Markers (marcas en cada interseccion de datos):
-   Point marker
,   Pixel marker
o   Circle marker
v   Triangle_down marker
^   Triangle_up marker
<   Triangle_left marker
>   Triangle_right marker
1   Tri_down marker
2   Tri_up marker
3   Tri_left marker
4   Tri_right marker
''''''
linestyle (Estilo de la linea)
-   Solid line style
--  Dashed line style
-.  Dash-dot line style
:   Dotted line style
''''''
color (color de la linea)
b   Blue
g   Green
r   Red
c   Cyan
m   Magenta
y   Yellow
k   Black
w   White
''''''
legend(loc="")
best            0
upper right     1
upper left      2
lower left      3
lower right     4
right           5
center left     6  
center right    7
lower center    8
upper center    9
center          10
'''
#Grafico de Linea = Line Plot
plt.figure(figsize=(10,6))  #Cambiar el tamaño del grafico

x = [2016,2017,2018,2019,2020,2021]
y = [42,43,45,47,48,50]

x2 = [2016,2017,2018,2019,2020,2021]
y2 = [43,43,44,44,45,45]


plt.plot(x2,y2,marker = "^",linestyle = "--", color ="b",label="Rep.Dom")
plt.plot(x,y,marker = "o",linestyle = "-", color ="r",label="Haiti")
plt.xlabel("Años")  #Agregamos un label al eje X
plt.ylabel("Poblacion")  #Agregamos un label al eje Y
plt.title("Años VS poblacion")  #Agregamos un titulo a la grafica
plt.yticks([46,39,51])   #Configuramos para que se vean algunos datos

plt.savefig("Ejemplo.png") #guardar grafica

#Mostrar leyenda, debe estar relacionada con el parametro "label" de la linea
plt.legend(loc = 4)
plt.show()  #mostramos el grafico

#####################################################################################################
#Graficos de barras = Bar Plots

xx = ["Argentina","Colombia","Peru"]
yy = [40,50,33]

plt.bar(xx,yy)
plt.show()


#####################################################################################################
#Graficos de Pastel = Piecharts

plt.pie(yy,labels=xx)
plt.show()


#####################################################################################################
#Histogramas = Histogram
#Solo admite datos numericos
edades = [15,16,17,20,21,21,22,23,24,25,26,30,31,32,35]
bins = [15,20,25,30,35]

plt.hist(edades,bins,edgecolor ="yellow")
plt.show()



#####################################################################################################
#Grafico de cajas = Boxplots
#Solo admite datos numericos
plt.boxplot(edades)
plt.show()


#####################################################################################################
#Grafico de dispersion = scatterplot

a = [1,2,3,4,5,4,3,2,2,4,5,6,7]
b = [7,2,3,5,5,7,3,2,1,4,6,3,2]

plt.scatter(a,b)
plt.show()

#####################################################################################################
#Grafico de dispersion = subplots

fig, ax = plt.subplots(1,2,sharey=True) #fila,columnas. "sharey alinear ejes"

ax[0].plot(x,y,color="y")
ax[1].plot(x2,y2,color="r")
plt.show()