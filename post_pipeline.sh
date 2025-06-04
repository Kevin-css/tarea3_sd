#!/bin/bash
source /etc/profile
cd /app

echo "🚀 Ejecutando main.py para generar eventos simulados..."
python main.py

echo "🧼 Limpiando salidas anteriores de Pig..."
rm -rf salida_local/

echo "📊 Ejecutando script de Apache Pig..."
pig -x local procesar_eventos.pig

echo "📁 Copiando resultados de Pig a archivos .csv..."
mkdir -p exportados

if [ -f salida_local/por_comuna/part-r-00000 ]; then
  cp salida_local/por_comuna/part-r-00000 exportados/num_eventos_xcomuna.csv
else
  echo "⚠️ Advertencia: No se encontró salida_local/por_comuna/part-00000"
fi

if [ -f salida_local/por_tipo/part-r-00000 ]; then
  cp salida_local/por_tipo/part-r-00000 exportados/num_eventos_xtipo.csv
else
  echo "⚠️ Advertencia: No se encontró salida_local/por_tipo/part-00000"
fi

if [ -f salida_local/por_fecha/part-r-00000 ]; then
  cp salida_local/por_fecha/part-r-00000 exportados/num_eventos_xfecha.csv
else
  echo "⚠️ Advertencia: No se encontró salida_local/por_fecha/part-00000"
fi

echo "📊 Generando gráficos de análisis exploratorio..."
python visualizador_csv.py


echo "✅ Flujo completo terminado. Archivos CSV exportados en carpeta 'exportados/'"

