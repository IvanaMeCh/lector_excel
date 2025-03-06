import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")


def get_dataframe(file_name, input_format="xlsx", base_path="files/"):
    """
    Convert file to pandas DataFrame and optionally save as CSV

    Args:
        file_name (str): Name of the file without extension
        input_format (str): Input file format ('xlsx' or 'xls')
        base_path (str): Base path for input/output files

    Returns:
        pandas.DataFrame: The converted data
    """
    try:
        if input_format.lower() in ["xlsx", "xls"]:
            df = pd.read_excel(f"{base_path}input/{file_name}.{input_format}")
            return df
        else:
            raise ValueError("Unsupported file format. Use 'xlsx' or 'xls'")
    except Exception as e:
        print(f"Error processing file: {e}")
        return None
    # Example usage:
    # datos_marangatu = get_dataframe("libro-compras-marangatu")

    # datos_abaco = get_dataframe("libro-compras-abaco")


def save_dataframe_to_csv(df, file_name, base_path="files/output/"):
    """
    Save DataFrame to CSV file

    Args:
        df (pandas.DataFrame): DataFrame to save
        file_name (str): Name of the file without extension
        base_path (str): Base path for input/output files
    """
    try:
        df.to_csv(f"{base_path}{file_name}.csv", index=False)
        print(f"File saved as {file_name}.csv")
    except Exception as e:
        print(f"Error saving file: {e}")
    # Example usage:
    # save_dataframe_to_csv(datos_marangatu, "datos-marangatu")

    # save_dataframe_to_csv(datos_abaco, "datos-abaco")


def limpiar_df(df, tipo):
    try:
        if tipo == "abaco":
            df = df.iloc[6:-3].reset_index(drop=True)
            new_headers = [
                "Fecha",
                "Tipo de timbrado",
                "Comprobante",
                "Serie",
                "CDC",
                "Timbrado",
                "Venc.",
                "Razon social",
                "RUC",
                "DV",
                "GRAV. 10%",
                "GRAV. 5%",
                "IVA 10%",
                "IVA 5%",
                "EXENTAS",
                "BASE IMP.",
                "Total",
                "MON.",
                "Condicion",
                "Cuotas",
                "Tipo",
                "Observacion",
                "Cuentas contables",
                "FORMULARIO 145",
                "Motivos inclusion",
                "Detalles inclusion",
                "Motivo anulado",
            ]
            df.columns = new_headers
            for col in ["Comprobante", "Timbrado", "Total"]:
                df[col] = df[col].astype(str).str.strip()
            df.set_index(["Timbrado", "Comprobante"], inplace=True)
            return df
        if tipo == "marangatu":
            new_headers = [
                "RUC del Informante",
                "Nombre o Razon Social del Informante",
                "RUC / Nº de Identificacion del Informado",
                "Tipo de Identificación del Informado",
                "Razon social",
                "Tipo de Registro",
                "Tipo de Comprobante",
                "Fecha de Emisión",
                "Periodo de Emision",
                "Condicion de la Operacion",
                "Operación en Moneda Extranjera",
                "Timbrado",
                "Comprobante",
                "CDC",
                "Monto Gravado 10%",
                "IVA 10%",
                "Monto Gravado 5%",
                "IVA 5%",
                "Monto No Gravado / Exento",
                "Total",
                "Imputa IVA",
                "Imputa IRE",
                "Imputa IRP",
                "No Imputar",
                "Numero de Comprobante Asociado",
                "Timbrado del Comprobante Asociado",
                "Fecha de Registro",
                "Origen de la Información",
            ]
            df.columns = new_headers
            for col in ["Comprobante", "Timbrado", "Total"]:
                df[col] = df[col].astype(str).str.strip()
            df.set_index(["Timbrado", "Comprobante"], inplace=True)
            return df

    except Exception as e:
        print(f"Error procesando archivo: {e}")
        return None


def verificar_existencia_comprobante(timbrado, comprobante, df_abaco, df_marangatu):
    """
    Verifica si un comprobante existe en uno o ambos DataFrames

    Args:
        timbrado (str): Número de timbrado
        comprobante (str): Número de comprobante
        df_abaco (DataFrame): DataFrame de Abaco
        df_marangatu (DataFrame): DataFrame de Marangatu

    Returns:
        str: Mensaje indicando dónde existe el comprobante
    """
    existe_abaco = False
    existe_marangatu = False

    try:
        df_abaco.loc[timbrado, comprobante]
        existe_abaco = True
    except KeyError:
        pass

    try:
        df_marangatu.loc[timbrado, comprobante]
        existe_marangatu = True
    except KeyError:
        pass

    if existe_abaco and existe_marangatu:
        return "El comprobante existe en ambos sistemas"
    elif existe_abaco:
        return "El comprobante existe solo en Abaco"
    elif existe_marangatu:
        return "El comprobante existe solo en Marangatu"
    else:
        return "El comprobante no existe en ningún sistema"
