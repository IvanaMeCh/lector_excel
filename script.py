from utils import (
    get_dataframe,
    save_dataframe_to_csv,
    limpiar_df,
    verificar_existencia_comprobante,
)
import pandas as pd


def generar_reporte_comparacion(df_abaco, df_marangatu):
    """
    Genera un reporte CSV que indica si cada comprobante está en Abaco, Marangatu, ambos o ninguno.

    Args:
        df_abaco (DataFrame): DataFrame de Abaco
        df_marangatu (DataFrame): DataFrame de Marangatu
    """
    # Obtener todos los índices únicos (timbrado, comprobante) de ambos DataFrames
    indices_abaco = set(df_abaco.index)
    indices_marangatu = set(df_marangatu.index)
    todos_indices = indices_abaco.union(indices_marangatu)

    # Crear listas para el nuevo DataFrame
    timbrados = []
    comprobantes = []
    estados = []

    # Analizar cada índice
    for timbrado, comprobante in todos_indices:
        timbrados.append(timbrado)
        comprobantes.append(comprobante)

        if (timbrado, comprobante) in indices_abaco and (
            timbrado,
            comprobante,
        ) in indices_marangatu:
            estados.append("En ambos")
        elif (timbrado, comprobante) in indices_abaco:
            estados.append("Solo en Abaco")
        elif (timbrado, comprobante) in indices_marangatu:
            estados.append("Solo en Marangatu")
        else:
            estados.append("En ninguno")

    # Crear nuevo DataFrame
    df_reporte = pd.DataFrame(
        {"Timbrado": timbrados, "Comprobante": comprobantes, "Estado": estados}
    )

    # Guardar el reporte
    save_dataframe_to_csv(df_reporte, "reporte_comparacion")
    return df_reporte


# Obtener DataFrame
df_marangatu = get_dataframe("libro-compras-marangatu")
# print(df_marangatu.head())

df_abaco = get_dataframe("libro-compras-abaco")
# print(df_abaco.head())

df_limpio_abaco = limpiar_df(df_abaco, "abaco")
df_limpio_marangatu = limpiar_df(df_marangatu, "marangatu")
# Guardar los DataFrames limpios en archivos CSV
save_dataframe_to_csv(df_limpio_abaco, "df_limpio_abaco")
save_dataframe_to_csv(df_limpio_marangatu, "df_limpio_marangatu")

comprobante = "003-001-0032961"
timbrado = "15841244"

comprobante2 = "001-002-0009418"
timbrado2 = "16094945"

comprobante3 = "001-001-0096426"
timbrado3 = "15995952"
# print(df_limpio_abaco.loc[timbrado, comprobante]["Total"])
# print("--------------------------------")
# print(df_limpio_marangatu.loc[timbrado, comprobante]["Total"])

# Ejemplo de uso
resultado = verificar_existencia_comprobante(
    timbrado3, comprobante3, df_limpio_abaco, df_limpio_marangatu
)
print(resultado)

# Generar y guardar el reporte de comparación
df_reporte = generar_reporte_comparacion(df_limpio_abaco, df_limpio_marangatu)
print("Reporte de comparación generado exitosamente")
