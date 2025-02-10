import pandas as pd

base_path = "files/"
file_name = "libro-compras-marangatu"
datos_excel = pd.read_excel(f"{base_path}input/{file_name}.xlsx")
datos_excel.to_csv(f"{base_path}output/{file_name}.csv")

print(datos_excel.head(2))
