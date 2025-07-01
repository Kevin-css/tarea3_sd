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

