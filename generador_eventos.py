import random
from datetime import datetime, timedelta

def generar_eventos_simulados(n):
    tipos = [
        "Accidente", "Congestión", "Policía", "Peligro", "Obras viales", "Peatón atropellado", 
        "Vehículo detenido", "Choque múltiple", "Volcamiento", "Corte de tránsito", 
        "Evento masivo", "Semáforo apagado", "Aluvión", "Incendio", "Manifestación", 
        "Lluvia intensa", "Niebla", "Desvío", "Moto accidentada", "Tránsito detenido"
    ]

    comunas = [
        "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", 
        "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", 
        "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", 
        "Peñalolén", "Providencia", "Pudahuel", "Puente Alto", "Quilicura", "Quinta Normal", 
        "Recoleta", "Renca", "San Joaquín", "San Miguel", "San Ramón", "Santiago", 
        "Vitacura"
    ]

    eventos = []
    fecha_inicio = datetime(2024, 1, 1)
    for i in range(n):
        evento = {
            "id": i,
            "lat": round(random.uniform(-33.75, -33.3), 6),
            "lng": round(random.uniform(-70.9, -70.4), 6),
            "tipo": random.choice(tipos),
            "comuna": random.choice(comunas),
            "fecha": (fecha_inicio + timedelta(minutes=random.randint(0, 525600))).strftime("%Y-%m-%d"),
            "descripcion": f"Incidente #{i}"
        }
        eventos.append(evento)
    return eventos

