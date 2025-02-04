import pandas as pd #importamos pandas para manejar datos en python 

#nombramos el archivo de excel
archivo_excel = "compras.xlsx"

#leemos el archivo de excel 
df= pd.read_excel(archivo_excel, engine="openpyxl")

#Mostramos en la consola
print(df)