import pandas as pd
from utils import get_dataframe, save_dataframe_to_csv, limpiar_df

# Obtener DataFrame
df_marangatu = get_dataframe("libro-compras-marangatu")
print(df_marangatu.head())

df_abaco = get_dataframe("libro-compras-abaco")
#print(df_abaco.head())

df_limpio_abaco = limpiar_df(df_abaco, "abaco")
#print(df_limpio_abaco.head())
save_dataframe_to_csv(df_limpio_abaco, "abaco")


df_limpio_marangatu = limpiar_df(df_marangatu, "marangatu")
save_dataframe_to_csv(df_limpio_marangatu, "marangatu")
