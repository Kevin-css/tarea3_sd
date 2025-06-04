# visualizador_csv.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")

EXPORT_DIR = "exportados"
GRAFICOS_DIR = "graficos_analisis"
os.makedirs(GRAFICOS_DIR, exist_ok=True)

def graficar_comuna():
    df = pd.read_csv(os.path.join(EXPORT_DIR, "num_eventos_xcomuna.csv"), header=None, names=["comuna", "total"])
    df = df.sort_values(by="total", ascending=False)
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x="comuna", y="total", palette="viridis")
    plt.title("Número de eventos por comuna")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "eventos_por_comuna.png"))
    plt.close()

def graficar_tipo():
    df = pd.read_csv(os.path.join(EXPORT_DIR, "num_eventos_xtipo.csv"), header=None, names=["tipo", "frecuencia"])
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="tipo", y="frecuencia", palette="rocket")
    plt.title("Frecuencia de tipos de incidentes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "frecuencia_tipos_incidentes.png"))
    plt.close()

def graficar_fecha():
    df = pd.read_csv(os.path.join(EXPORT_DIR, "num_eventos_xfecha.csv"), header=None, names=["fecha", "total_diario"])
    df["fecha"] = pd.to_datetime(df["fecha"], errors='coerce')
    df = df.sort_values("fecha")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x="fecha", y="total_diario", marker="o")
    plt.title("Evolución temporal de incidentes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(GRAFICOS_DIR, "eventos_por_fecha.png"))
    plt.close()

if __name__ == "__main__":
    print("📊 Generando visualizaciones a partir de los archivos CSV...")
    graficar_comuna()
    graficar_tipo()
    graficar_fecha()
    print(f"✅ Gráficos exportados en la carpeta '{GRAFICOS_DIR}/'")
