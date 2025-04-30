
# 🧠 Tarea 1 - Sistemas Distribuidos 2025-1

Este proyecto simula un sistema distribuido que recolecta, almacena y consulta eventos de tráfico utilizando herramientas modernas como Python, MongoDB y Docker. Inspirado en el sistema Waze, el sistema permite medir el rendimiento de distintas configuraciones de caché bajo patrones de tráfico simulados mediante distribuciones estadísticas.

---

## 📦 Estructura del Proyecto

```
Tarea_1_SD/
├── cache.py
├── config.py
├── docker-compose.yml
├── Dockerfile
├── evaluador.py
├── generador_eventos.py
├── generador_trafico.py
├── main.py
├── mongodb_client.py
├── README.md
└── graficos_local/
    ├── binomial_LRU.png
    ├── binomial_LFU.png
    ├── poisson_LRU.png
    └── poisson_LFU.png
```

---

## 🚀 Instrucciones de Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Kevin-css/tarea1_sd.git
cd tarea1_sd
```

### 2. Ejecutar con Docker Compose

```bash
docker-compose up --build
```

Esto levantará dos contenedores:

- `mongo`: Base de datos MongoDB
- `sistema_sd`: Sistema Python que:
  - Genera eventos simulados
  - Inserta los eventos en MongoDB
  - Simula tráfico
  - Evalúa distintas configuraciones de caché
  - Genera gráficos con los resultados

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

Los gráficos generados se guardan automáticamente en la carpeta `graficos_local/`. Estos muestran la tasa de aciertos (hit rate) según política de caché, tamaño del caché, número de consultas y distribución de tráfico utilizada.

---

## 📁 Archivos Clave

- `main.py`: Punto de entrada del sistema
- `generador_eventos.py`: Crea los eventos simulados con ID, latitud, longitud y tipo
- `generador_trafico.py`: Simula consultas usando distribuciones estadísticas
- `evaluador.py`: Ejecuta las combinaciones de evaluación y genera los gráficos
- `cache.py`: Define las políticas LRU y LFU usando `cachetools`
- `mongodb_client.py`: Conecta a la base de datos MongoDB
- `config.py`: Permite configurar los parámetros del sistema

---

## 📈 Análisis de Resultados

- Las tasas de acierto aumentan consistentemente con tamaños mayores de caché.
- LFU obtiene mejores resultados en distribuciones donde hay eventos repetidos frecuentemente (como Poisson), ya que premia la frecuencia.
- LRU funciona bien en situaciones más distribuidas o aleatorias (como ciertas configuraciones de Binomial).
- Los valores bajos de caché muestran un desempeño significativamente menor, lo que demuestra la importancia de una buena política de remoción combinada con un tamaño adecuado de almacenamiento temporal.
- El sistema, pese a ser simulado, refleja correctamente fenómenos reales como saturación del caché, repetición de accesos y penalización por consultas únicas.

---

## 🧪 Tecnologías Utilizadas

- Python 3.10+
- Docker y Docker Compose
- MongoDB
- NumPy
- Pandas
- Matplotlib
- cachetools

---

## 📜 Licencia

Este proyecto es parte de la entrega del curso "Sistemas Distribuidos - Universidad Diego Portales (2025-1)". 
