import json
import csv

with open (r"C:\Users\Usuario\Desktop\cursoPythonAvanzado\tp3_Puerari\user.json", "r") as archivo_json:
    datos = json.load(archivo_json)

user_csv = "datos.csv"
with open (user_csv, 'w', newline = "") as archivo_csv:
    # Utilizamos DictWriter para escribir datos en formato CSV
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=datos[0].keys())

    escritor_csv.writeheader()
    escritor_csv.writerows(datos)