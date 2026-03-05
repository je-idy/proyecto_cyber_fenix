# persistencia de datos de archivos
from pathlib import Path
import json
import csv

DATA_DIR = Path(__file__).parent / "data"
TXT_FILE = DATA_DIR / "datos.txt"
CSV_FILE = DATA_DIR / "datos.csv"

# ASEGURAR LA DATA
def asegurar_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

# Guardar datos en un archivo de texto

def guardar_txt(registro: str):
    asegurar_data_dir()
    with open(TXT_FILE, 'a', encoding='utf-8') as f:
        f.write(registro + '\n')

# leer datos de un archivo de texto
def leer_txt():
    asegurar_data_dir()
    if not TXT_FILE.exists():
        return []
    with open(TXT_FILE, 'r', encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

# JSON
def guardar_json(dic):
    asegurar_data_dir()
    data = leer_json()
    data.append(dic)
    with open(DATA_DIR / "datos.json", 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# leer json
def leer_json():
    asegurar_data_dir()
    json_file = DATA_DIR / "datos.json"
    if not json_file.exists():
        return []
    with open(json_file, 'r', encoding="utf-8") as f:
        return json.load(f)

# CSV
def guardar_csv(dic: dict):
    asegurar_data_dir()
    existe = CSV_FILE.exists()

    with open(CSV_FILE, 'a', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)

        if not existe:
            writer.writerow(['nombre', 'descripcion', 'cantidad', 'precio'])

        writer.writerow([
            dic['nombre'],
            dic['descripción'],
            dic['cantidad'],
            dic['precio']
        ])
# Leer CSV
def leer_csv():
    asegurar_data_dir()
    if not CSV_FILE.exists():
        return []

    datos = []

    with open(CSV_FILE, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # saltar encabezado

        for row in reader:
            if row:
                datos.append({
                    "nombre": row[0],
                    "descripcion": row[1],
                    "cantidad": row[2],
                    "precio": row[3]
                })

    return datos