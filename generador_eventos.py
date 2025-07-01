import random
import csv
import os
import time
from datetime import datetime, timedelta
from collections import Counter

# Crear carpeta de exportación si no existe
os.makedirs("exportados", exist_ok=True)

# Comunas ponderadas según flujo vehicular real aproximado
comunas = (
    ["Santiago"] * 12 + ["Puente Alto"] * 10 + ["Maipú"] * 10 + ["La Florida"] * 9 +
    ["Ñuñoa"] * 8 + ["Las Condes"] * 8 + ["Pudahuel"] * 6 + ["Estación Central"] * 6 +
    ["Providencia"] * 6 + ["Recoleta"] * 5 + ["San Miguel"] * 5 + ["Peñalolén"] * 5 +
    ["Macul"] * 5 + ["Renca"] * 4 + ["Huechuraba"] * 4 + ["La Pintana"] * 4 +
    ["Lo Prado", "San Joaquín", "San Ramón", "La Granja", "Pedro Aguirre Cerda", "Conchalí"] * 3 +
    ["Lo Barnechea", "Vitacura", "La Reina", "Independencia", "Cerro Navia", "La Cisterna", "Quilicura", "Quinta Normal"]
)

# Tipos de eventos ponderados por frecuencia realista
tipos = [
    "Accidente", "Congestión", "Policía", "Peligro", "Obras viales", "Peatón atropellado",
    "Vehículo detenido", "Choque múltiple", "Volcamiento", "Corte de tránsito",
    "Evento masivo", "Semáforo apagado", "Aluvión", "Incendio", "Manifestación",
    "Lluvia intensa", "Niebla", "Desvío", "Moto accidentada", "Tránsito detenido"
]
pesos_tipos = [
    15, 25, 7, 5, 10, 3,
    10, 3, 2, 4,
    2, 3, 1, 2, 5,
    3, 1, 3, 3, 8
]

def generar_eventos_simulados(n):
    eventos = []
    fecha_inicio = datetime(2024, 1, 1)
    fecha_fin = datetime(2024, 12, 31)

    start_time = time.time()
    for i in range(n):
        minutos_totales = int((fecha_fin - fecha_inicio).total_seconds() / 60)
        fecha_random = fecha_inicio + timedelta(minutes=random.randint(0, minutos_totales))

        evento = {
            "id": i,
            "lat": round(random.uniform(-33.75, -33.3), 6),
            "lng": round(random.uniform(-70.9, -70.4), 6),
            "tipo": random.choices(tipos, weights=pesos_tipos, k=1)[0],
            "comuna": random.choice(comunas),
            "fecha": fecha_random.strftime("%Y-%m-%d"),
            "descripcion": f"Incidente #{i} en zona urbana"
        }
        eventos.append(evento)

    duracion = time.time() - start_time
    #guardar_csv_eventos(eventos)
    guardar_metricas_scraper(eventos, duracion)
    return eventos

def guardar_csv_eventos(eventos):
    with open("exportados/eventos_simulados.csv", mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=eventos[0].keys())
        writer.writeheader()
        writer.writerows(eventos)

def guardar_metricas_scraper(eventos, duracion_scrape):
    ruta_csv = "exportados/metricas_scraper.csv"
    headers = ["timestamp", "duracion_segundos", "eventos_recolectados", "status"]

    metricas = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "duracion_segundos": round(duracion_scrape, 3),
        "eventos_recolectados": len(eventos),
        "status": "SUCCESS" if len(eventos) > 0 else "FAIL"
    }

    escribir_encabezado = not os.path.exists(ruta_csv)

    with open(ruta_csv, mode="a", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=headers)
        if escribir_encabezado:
            writer.writeheader()
        writer.writerow(metricas)
