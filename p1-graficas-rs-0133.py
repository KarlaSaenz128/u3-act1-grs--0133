import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# crearemos nuestra tabla y la guardaremos con pandas
# tenemos 6 listas de redes sociales con 4 elementos por lista 
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkedin', 7277, False, 2012]

# creamos una lista de listas (conformando la tabla)
listas_redes_sociales = [fb, twt, ig, wsp, tel, lkn]

#print(listas_redes_sociales)
# utilizar pandas para organizar la tabla (datafarme o marco de datos)
# a cada columna le ponemos nombre
df_redes_sociales = pd.DataFrame(listas_redes_sociales, columns=["Nombre", "Cantidad", "Es_FB", "Año"])
print(df_redes_sociales)

# cremos el archivo CSV y lo guardamos en CSV
# df_redes_sociales.to_csv("redessociales.csv", index=False)

# crear grafica de lineas 
# donde X es Nombre en el eje horizontal
# donde y es Nombre en el eje vertical
plt.plot(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title("Graficas redes sociales 0133")
plt.xlabel("Numero de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()

# crear una grafica de puntos
plt.scatter(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title("Graficas redes sociales 0133")
plt.xlabel("Numero de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()

## Grafica de barras (sin ordenar)
plt.bar(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title("Redes Sociales 0133")
plt.xlabel("Las redes")
plt.ylabel("cantidad usuarios")
# 3. Mostrar la gráfica
plt.show()

# ordenar la grafica de barras de manera descendente
# de la mas grande a la mas pequeña
df_rs_ordenar = df_redes_sociales.sort_values("Cantidad", ascending=False)
plt.bar(df_rs_ordenar["Nombre"], df_rs_ordenar["Cantidad"])
plt.title("Redes Sociales 0133 (Ordenadas)")
plt.xlabel("Las redes")
plt.ylabel("cantidad usuarios")
plt.show()

# coloreando la grafica 
df_rs_ordenar = df_redes_sociales.sort_values("Cantidad", ascending=False)
plt.bar(df_rs_ordenar["Nombre"], df_rs_ordenar["Cantidad"], color=["b", "g", "c", "y", "r", "m"])
plt.title("Redes Sociales 0133 (Ordenadas)")
plt.xlabel("Las redes")
plt.ylabel("cantidad usuarios")
plt.show()

# Grafica de pastel 
#plt.plot(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.pie(df_redes_sociales["Cantidad"],labels=df_redes_sociales["Nombre"])
plt.title("Redes Sociales 0133 (Distribución)")
plt.show()
