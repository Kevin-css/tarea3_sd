import time
import matplotlib.pyplot as plt
import pandas as pd
import os
from cache import crear_cache
from mongodb_client import conectar_mongo
from config import CONFIGS_EVALUACION, LAMBDA_POISSON, P_BINOMIAL
from generador_trafico import generar_consultas

def evaluar_configuracion(n_consultas, cache_policy, cache_size, distribucion):
    db = conectar_mongo()
    eventos = db.eventos
    ids_eventos = [e["id"] for e in eventos.find({}, {"_id": 0, "id": 1})]

    consultas = generar_consultas(ids_eventos, n_consultas, distribucion, LAMBDA_POISSON, P_BINOMIAL)
    cache = crear_cache(cache_policy, cache_size)

    aciertos = 0
    inicio = time.time()

    for consulta in consultas:
        id_evento = consulta["id"]
        if id_evento in cache:
            aciertos += 1
        else:
            evento = eventos.find_one({"id": id_evento})
            if evento:
                cache[id_evento] = evento

    fin = time.time()
    tasa_acierto = (aciertos / len(consultas)) * 100

    return {
        "n_consultas": n_consultas,
        "cache_policy": cache_policy,
        "cache_size": cache_size,
        "distribucion": distribucion,
        "aciertos": aciertos,
        "tasa_acierto": round(tasa_acierto, 2),
        "tiempo": round(fin - inicio, 3)
    }

def evaluar_todas_las_configuraciones():
    resultados = []

    for distribucion in CONFIGS_EVALUACION["distribuciones"]:
        for cache_policy in CONFIGS_EVALUACION["cache_policies"]:
            for cache_size in CONFIGS_EVALUACION["cache_sizes"]:
                for n_consultas in CONFIGS_EVALUACION["n_consultas"]:
                    print(f"▶ Evaluando: {distribucion}, {cache_policy}, {cache_size}, {n_consultas}")
                    r = evaluar_configuracion(n_consultas, cache_policy, cache_size, distribucion)
                    resultados.append(r)

    return resultados

def graficar_resultados(resultados, ruta_salida="resultados_graficos"):
    df = pd.DataFrame(resultados)
    os.makedirs(ruta_salida, exist_ok=True)

    for distribucion in df["distribucion"].unique():
        for cache_policy in df["cache_policy"].unique():
            subset = df[(df["distribucion"] == distribucion) & (df["cache_policy"] == cache_policy)]

            for cache_size in sorted(subset["cache_size"].unique()):
                data = subset[subset["cache_size"] == cache_size]
                plt.plot(data["n_consultas"], data["tasa_acierto"], marker='o', label=f"Caché {cache_size}")

            plt.title(f"Tasa de aciertos - {distribucion.upper()} - {cache_policy}")
            plt.xlabel("Cantidad de consultas")
            plt.ylabel("Tasa de acierto (%)")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            filename = f"{ruta_salida}/{distribucion}_{cache_policy}.png"
            plt.savefig(filename)
            print(f"📊 Gráfico guardado en: {filename}")
            plt.close()

def ejecutar_evaluacion():
    print("🧪 Iniciando evaluación automatizada...")
    resultados = evaluar_todas_las_configuraciones()
    graficar_resultados(resultados)

if __name__ == "__main__":
    ejecutar_evaluacion()
