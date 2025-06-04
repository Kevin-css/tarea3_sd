
# 🧠 Tarea 2 - Sistemas Distribuidos 2025-1

Este proyecto simula un sistema distribuido que recolecta, almacena, consulta y analiza eventos de tráfico utilizando herramientas modernas como Python, MongoDB, Docker y Apache Pig. Inspirado en el sistema Waze, permite evaluar configuraciones de caché y realizar procesamiento distribuido para obtener métricas agregadas relevantes para tomadores de decisiones como la Unidad de Control de Tránsito y municipios de la Región Metropolitana.


---

## 📦 Estructura del Proyecto

```
Tarea_2_SD/
├── cache.py
├── config.py
├── docker-compose.yml
├── Dockerfile
├── evaluador.py
├── exportador_csv.py
├── generador_eventos.py
├── generador_trafico.py
├── main.py
├── mongodb_client.py
├── procesar_eventos.pig
├── README.md
├── resultados_graficos/
│ ├── binomial_LRU.png
│ ├── binomial_LFU.png
│ ├── poisson_LRU.png
│ └── poisson_LFU.png
├── exportados/
│ └── eventos.csv
└── salida_local/
├── por_comuna/
├── por_tipo/
└── por_fecha/

```

---

## 🚀 Instrucciones de Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Kevin-css/tarea2_sd.git 
cd tarea2_sd
```

### 2. Ejecutar con Docker Compose

```bash
docker-compose up --build
```

Esto levantará dos contenedores:

- `mongo`: Base de datos MongoDB
- `sistema_sd`: Sistema en Python que:
  - Genera 10.000 eventos de tráfico con fechas, comunas y tipos variados.
  - Inserta los eventos en MongoDB
  - Simula tráfico y realiza evaluaciones de rendimiento usando caché (LRU y LFU).
  - Evalúa distintas configuraciones de caché
  - Exporta los eventos a un archivo CSV
  - Genera gráficos con los resultados
  - Ejecuta automáticamente un script Apache Pig para agrupar y analizar los datos por comuna, tipo de incidente y fecha
  - Exporta los resultados del procesamiento en Pig a archivos CSV listos para análisis exploratorio

---

## ⚙️ Configuración

Edita el archivo `config.py` para modificar los parámetros de evaluación:

```python
N_EVENTOS = 10000  # Número fijo de eventos simulados

LAMBDA_POISSON = 1    # λ para la distribución Poisson
P_BINOMIAL = 0.5      # p para la distribución Binomial

CONFIGS_EVALUACION = {
    "n_consultas": [500, 1000, 3000, 5000],
    "cache_policies": ["LRU", "LFU"],
    "cache_sizes": [50, 200, 500, 1500],
    "distribuciones": ["poisson", "binomial"]
}
```

---

## 📊 Resultados

- Los gráficos generados se guardan automáticamente en la carpeta `graficos_local/`. Estos muestran la tasa de aciertos (hit rate) según política de caché, tamaño del caché, número de consultas y distribución de tráfico utilizada.

- Los resultados agregados para esta parte 2 de Apache Pig se exportan como archivos .csv en la carpeta salida_local/,  con las siguientes categorías:

  - `por_comuna`: Total de incidentes por comuna.

  - `por_tipo`: Frecuencia de tipos de incidentes.

  - `por_fecha`: Evolución temporal de los eventos.

y posteriormente se traspasan a la carpeta exportados donde dichos archivo se tranforman a .csv y con ello se logra realizar un analisis. Y luego graficar los resultados que se muentran en la carpeta `graficos_analisis/`

---

## 📁 Archivos Clave

- `main.py`: Punto de entrada del sistema
- `generador_eventos.py`: Crea los eventos simulados con ID, latitud, longitud y tipo
- `generador_trafico.py`: Simula consultas usando distribuciones estadísticas
- `evaluador.py`: Ejecuta las combinaciones de evaluación y genera los gráficos
- `cache.py`: Define las políticas LRU y LFU usando `cachetools`
- `mongodb_client.py`: Conecta a la base de datos MongoDB
- `config.py`: Permite configurar los parámetros del sistema
- `procesar_eventos.pig`: Script de procesamiento distribuido en Apache Pig.
- `exportador_csv.py`: Exporta eventos desde MongoDB a eventos.csv.
- `Dockerfile`: Conteneriza el sistema, instala Java, Pig y configura entorno.
- `docker-compose.yml`: Orquesta servicios para MongoDB y sistema Python.
- `visualizador_csv.py`: Permite graficar los datos obtenidos mediante el procesamiento en apache pig 

---

## 📈 Análisis de Resultados

Parte 1:

- Las tasas de acierto aumentan consistentemente con tamaños mayores de caché.
- LFU obtiene mejores resultados en distribuciones donde hay eventos repetidos frecuentemente (como Poisson), ya que premia la frecuencia.
- LRU funciona bien en situaciones más distribuidas o aleatorias (como ciertas configuraciones de Binomial).
- Los valores bajos de caché muestran un desempeño significativamente menor, lo que demuestra la importancia de una buena política de remoción combinada con un tamaño adecuado de almacenamiento temporal.
- El sistema, pese a ser simulado, refleja correctamente fenómenos reales como saturación del caché, repetición de accesos y penalización por consultas únicas.

Parte 2:

- El sistema permite ahora:

- Realizar un análisis exploratorio automático sobre los datos procesados, útil para detectar patrones espaciales, temporales o por tipo de incidente lo cual se detalla mas en el informe junto con los graficos respectivos. O bien pueden verse en la carpeta `graficos_analisis/`


---

## 🧪 Tecnologías Utilizadas

- Python 3.10+
- Docker y Docker Compose
- Apache Pig
- MongoDB
- NumPy
- Pandas
- Matplotlib
- cachetools

---

## 📜 Licencia

Este proyecto es parte de la entrega del curso "Sistemas Distribuidos - Universidad Diego Portales (2025)". 
