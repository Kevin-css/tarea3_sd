import csv
import os
from mongodb_client import conectar_mongo

def exportar_eventos_a_csv(ruta="exportados/eventos.csv"):
    print("💾 Exportando eventos a CSV...")

    db = conectar_mongo()
    eventos = list(db.eventos.find({}, {"_id": 0}))  # Excluye el campo _id

    # Asegura que la carpeta exista
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    # Si no hay eventos, no exportar
    if not eventos:
        print("⚠ No hay eventos para exportar.")
        return

    # Tomar encabezados desde las claves del primer evento
    encabezados = eventos[0].keys()

    with open(ruta, mode="w", newline="", encoding="utf-8") as archivo_csv:
        escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(eventos)

    print(f"✅ Eventos exportados a: {ruta}")
