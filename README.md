# 🧠 Tarea 3: Sistema Distribuido de Análisis de Tráfico

Este proyecto implementa un sistema distribuido de extremo a extremo que recolecta, almacena, procesa y visualiza eventos de tráfico de la Región Metropolitana. El sistema utiliza **Python** para la recolección, **MongoDB** como base de datos primaria, **Apache Pig** para el procesamiento distribuido de datos y el **Stack Elástico (Elasticsearch y Kibana)** para la visualización interactiva de métricas y análisis.

El objetivo final es proporcionar una herramienta que permita a tomadores de decisiones, como la Unidad de Control de Tránsito, explorar patrones de tráfico de manera dinámica y eficiente.

---

## 🏗️ Arquitectura del Sistema

El flujo de datos sigue el siguiente pipeline:

1. **Scraper (Python)**: Recolecta eventos de tráfico (simulados, inspirados en Waze).
2. **Data Storage (MongoDB)**: Almacena los eventos en bruto.
3. **Procesamiento (Apache Pig)**: Procesa los datos para limpiar, filtrar y agregar métricas clave (incidentes por comuna, tipo y fecha).
4. **Indexación (Elasticsearch)**: Un exportador en Python toma los datos procesados por Pig y los indexa en Elasticsearch, preparándolos para búsquedas y visualizaciones rápidas.
5. **Visualización (Kibana)**: Kibana se conecta a Elasticsearch para mostrar los datos en un dashboard interactivo con gráficos, mapas y tablas.

---

## 🚀 Instrucciones de Ejecución

### 1. Prerrequisitos

* Tener instalado **Docker** y **Docker Compose**.

### 2. Clonar el Repositorio

```bash
git clone https://github.com/Kevin-css/tarea2_sd.git 
cd tarea2_sd

### 3. Ejecutar el Sistema Completo

```bash
docker-compose up --build
```

Este comando levantará cuatro servicios orquestados:

- **mongodb**: La base de datos para los datos en bruto.
- **elasticsearch**: El motor de búsqueda y analítica que almacena los datos procesados.
- **kibana**: La plataforma de visualización.
- **app**: El contenedor de Python que ejecuta el pipeline:
  - Genera y guarda los eventos en MongoDB.
  - Ejecuta el script de Apache Pig para procesar los datos.
  - Ejecuta el script `exportador_elastic.py` para enviar los resultados de Pig a Elasticsearch.
  - Genera logs de rendimiento del scraper y del caché, y los envía a Elasticsearch.

### 4. Acceder a Kibana

Una vez que los contenedores estén corriendo, abre tu navegador y ve a:

```bash
http://localhost:5601
```

Dentro de Kibana, podrás crear las visualizaciones y el dashboard para explorar los datos del tráfico.

📁 **Archivos Clave del Proyecto**

```
Tarea_3_SD/
├── docker-compose.yml     # Orquesta todos los servicios
├── Dockerfile             # Configura el contenedor de la aplicación Python
├── exportador_elastic.py  # Envía datos de CSV a Elasticsearch
├── procesar_eventos.pig   # Script de Pig para el análisis de datos
├── main.py                # Punto de entrada que ejecuta el pipeline
├── config.py              # Parámetros de configuración del sistema
├── generador_eventos.py   # Simula los eventos de tráfico
├── cache.py               # Lógica del sistema de caché
└── ... otros archivos del sistema
```

📊 **Resultados y Análisis**

A diferencia de las etapas anteriores, el resultado final de este proyecto no son gráficos estáticos, sino un dashboard interactivo en Kibana. Esta plataforma permite un análisis mucho más profundo y dinámico de los datos.

**Funcionalidades del Dashboard:**

- **Visualización Integrada**: El panel de control unifica métricas de rendimiento del sistema (logs del scraper y caché) con los datos de negocio (incidentes de tráfico).
- **Análisis Multidimensional**: Se pueden explorar los datos de tráfico clasificados por:
  - **Geografía**: Gráfico de barras con el total de incidentes por comuna.
  - **Tipología**: Gráfico de torta que desglosa los incidentes por su tipo (choque, congestión, etc.).
  - **Temporalidad**: Gráfico de líneas que muestra la evolución de los incidentes a lo largo del tiempo.
- **Interactividad y Filtrado Dinámico**: La principal ventaja del sistema es la capacidad de filtrar los datos en tiempo real. Al hacer clic en una comuna o un tipo de incidente en un gráfico, todos los demás gráficos del dashboard se actualizan automáticamente para reflejar la selección, permitiendo descubrir patrones complejos de manera intuitiva.

Este sistema distribuido completo demuestra cómo transformar datos en bruto en conocimiento accionable, proveyendo una herramienta visual poderosa para la toma de decisiones informadas en la gestión del tráfico urbano.

🛠️ **Tecnologías Utilizadas**

- **Lenguaje**: Python 3.10+
- **Contenerización**: Docker y Docker Compose
- **Base de Datos Primaria**: MongoDB
- **Procesamiento de Datos**: Apache Pig
- **Búsqueda y Analítica**: Elasticsearch
- **Visualización**: Kibana
- **Librerías Python**: elasticsearch, pymongo, pandas, etc.

📜 **Licencia**

Este proyecto es parte de la entrega del curso "Sistemas Distribuidos - Universidad Diego Portales (2025)".
