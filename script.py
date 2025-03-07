from utils import (
    get_dataframe,
    limpiar_df,
    separar_dataframes,
    save_dataframe_to_csv,
)


# Obtener DataFrame
df_marangatu = get_dataframe("libro-compras-marangatu")
df_abaco = get_dataframe("libro-compras-abaco")

# Limpiar DataFrames
df_limpio_abaco = limpiar_df(df_abaco, "abaco")
df_limpio_marangatu = limpiar_df(df_marangatu, "marangatu")

# Asumiendo que ya tienes los DataFrames limpios, separarlos
resultados = separar_dataframes(df_limpio_abaco, df_limpio_marangatu)

if resultados:
    # Acceder a los DataFrames resultantes
    solo_abaco = resultados["solo_abaco"]
    solo_marangatu = resultados["solo_marangatu"]
    coincidentes_abaco = resultados["coincidentes_abaco"]
    coincidentes_marangatu = resultados["coincidentes_marangatu"]

    # Imprimir información sobre los resultados
    print(f"Registros solo en Abaco: {len(solo_abaco)}")
    print(f"Registros solo en Marangatu: {len(solo_marangatu)}")
    print(f"Registros coincidentes: {len(coincidentes_abaco)}")

    # Guardar los DataFrames resultantes en archivos CSV
    save_dataframe_to_csv(solo_abaco, "solo_abaco")
    save_dataframe_to_csv(solo_marangatu, "solo_marangatu")
    save_dataframe_to_csv(coincidentes_abaco, "coincidentes_abaco")
    save_dataframe_to_csv(coincidentes_marangatu, "coincidentes_marangatu")
