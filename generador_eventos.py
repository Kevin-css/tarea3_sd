import random

def generar_eventos_simulados(n):
    tipos = ["Accidente", "Congestión", "Policía", "Peligro"]
    eventos = []
    for i in range(n):
        evento = {
            "id": i,
            "lat": round(random.uniform(-33.5, -33.3), 6),
            "lng": round(random.uniform(-70.7, -70.5), 6),
            "tipo": random.choice(tipos),
            "descripcion": f"Evento #{i}"
        }
        eventos.append(evento)
    return eventos
