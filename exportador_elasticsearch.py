import csv
import os
from elasticsearch import Elasticsearch, helpers

# Conexión a Elasticsearch
ELASTIC_URL = os.getenv("ELASTIC_URL", "http://localhost:9200")
es = Elasticsearch(ELASTIC_URL)

def eliminar_indice_si_existe(nombre_indice):
    if es.indices.exists(index=nombre_indice):
        es.indices.delete(index=nombre_indice)
        print(f"🗑️ Índice '{nombre_indice}' eliminado.")

def crear_indice_si_no_existe(nombre_indice, mapping):
    if not es.indices.exists(index=nombre_indice):
        es.indices.create(index=nombre_indice, body=mapping)
        print(f"✅ Índice '{nombre_indice}' creado con mapping.")
    else:
        print(f"ℹ️ Índice '{nombre_indice}' ya existe.")

def agregar_encabezado_si_falta(file_path, encabezados):
    with open(file_path, encoding='utf-8') as f:
        primera_linea = f.readline().strip()
        if primera_linea != ",".join(encabezados):
            f.seek(0)
            contenido = f.readlines()
            with open(file_path, mode='w', encoding='utf-8', newline='') as f_out:
                writer = csv.writer(f_out)
                writer.writerow(encabezados)
                for linea in contenido:
                    fila = linea.strip().split(",")
                    if len(fila) == len(encabezados):
                        writer.writerow(fila)

def index_csv(file_path, index_name):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        actions = [
            {
                "_index": index_name,
                "_source": {k: parse_val(v) for k, v in row.items()}
            }
            for row in reader
        ]
        helpers.bulk(es, actions)
        print(f"✅ Se indexaron {len(actions)} documentos en el índice '{index_name}'.")

def parse_val(value):
    value = value.strip()
    try:
        if value.lower() in ['true', 'false']:
            return value.lower() == 'true'
        return float(value) if '.' in value else int(value)
    except:
        return value

def exportador_elastic():
    base_path = "exportados"
    archivos = {
        "eventos.csv": "eventos",
        "num_eventos_xcomuna.csv": "eventos_xcomuna",
        "num_eventos_xfecha.csv": "eventos_xfecha",
        "num_eventos_xtipo.csv": "eventos_xtipo",
        "metricas_scraper.csv": "metricas_scraper",
        "metricas_cache.csv": "metricas_cache"
    }

    encabezados_por_archivo = {
        "num_eventos_xcomuna.csv": ["comuna", "num_eventos"],
        "num_eventos_xfecha.csv": ["fecha", "num_eventos"],
        "num_eventos_xtipo.csv": ["tipo", "num_eventos"],
        "metricas_scraper.csv": ["timestamp", "duracion_segundos", "eventos_recolectados", "status"],
        "metricas_cache.csv": ["timestamp", "consultas", "hits", "misses", "hit_rate", "miss_rate"]
    }

    mappings_generales = {
        "eventos": {
            "mappings": {
                "properties": {
                    "comuna": { "type": "keyword" },
                    "num_eventos": { "type": "integer" },
                    "fecha": { "type": "date" },
                    "tipo": { "type": "keyword" },
                    "lat": { "type": "float" },
                    "lng": { "type": "float" },
                    "descripcion": { "type": "text" },
                }
            }
        },
        "eventos_xcomuna": {
            "mappings": {
                "properties": {
                    "comuna": { "type": "keyword" },
                    "num_eventos": { "type": "integer" }
                }
            }
        },
        "eventos_xfecha": {
            "mappings": {
                "properties": {
                    "fecha": { "type": "date" },
                    "num_eventos": { "type": "integer" }
                }
            }
        },
        "eventos_xtipo": {
            "mappings": {
                "properties": {
                    "tipo": { "type": "keyword" },
                    "num_eventos": { "type": "integer" }
                }
            }
        },
        "metricas_scraper": {
            "mappings": {
                "properties": {
                    "timestamp": { "type": "date" },
                    "duracion_segundos": { "type": "float" },
                    "eventos_recolectados": { "type": "integer" },
                    "status": { "type": "keyword" }
                }
            }
        },
        "metricas_cache": {
            "mappings": {
                "properties": {
                    "timestamp": {
                        "type": "date",
                        "format": "yyyy-MM-dd HH:mm:ss"
                    },
                    "consultas": { "type": "integer" },
                    "hits": { "type": "integer" },
                    "misses": { "type": "integer" },
                    "hit_rate": { "type": "float" },
                    "miss_rate": { "type": "float" }
                }
            }
        }
    }

    for archivo, indice in archivos.items():
        ruta = os.path.join(base_path, archivo)
        if os.path.exists(ruta):
            if archivo in encabezados_por_archivo:
                agregar_encabezado_si_falta(ruta, encabezados_por_archivo[archivo])
            eliminar_indice_si_existe(indice)  # 👈 Elimina el índice anterior si existe
            crear_indice_si_no_existe(indice, mappings_generales[indice])
            index_csv(ruta, indice)
        else:
            print(f"⚠️ Archivo no encontrado: {ruta}")

if __name__ == "__main__":
    exportador_elastic()
