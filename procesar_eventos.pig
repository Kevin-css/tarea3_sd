-- ETAPA 1: Cargar los datos desde el CSV exportado por Python
eventos_raw = LOAD 'exportados/eventos.csv' USING PigStorage(',')
    AS (id:int, lat:float, lng:float, tipo:chararray, comuna:chararray, fecha:chararray, descripcion:chararray);

-- ETAPA 2: Preprocesamiento - Filtrar registros incompletos o nulos
eventos_limpios = FILTER eventos_raw BY 
    (lat IS NOT NULL AND lng IS NOT NULL AND comuna IS NOT NULL AND comuna != '' AND tipo IS NOT NULL AND tipo != '');

-- ETAPA 3: Clasificación y estructuración

-- 3.1 Agrupación por comuna
agrupados_comuna = GROUP eventos_limpios BY comuna;
conteo_comuna = FOREACH agrupados_comuna GENERATE 
    group AS comuna, COUNT(eventos_limpios) AS total_incidentes;

-- 3.2 Agrupación por tipo de incidente
agrupados_tipo = GROUP eventos_limpios BY tipo;
conteo_tipo = FOREACH agrupados_tipo GENERATE 
    group AS tipo_incidente, COUNT(eventos_limpios) AS frecuencia;

-- 3.3 Agrupación por fecha (análisis temporal)
agrupados_fecha = GROUP eventos_limpios BY fecha;
conteo_fecha = FOREACH agrupados_fecha GENERATE 
    group AS fecha, COUNT(eventos_limpios) AS total_diario;

-- ETAPA 4: Exportar resultados para análisis exploratorio
STORE conteo_comuna INTO 'salida_local/por_comuna' USING PigStorage(',');
STORE conteo_tipo INTO 'salida_local/por_tipo' USING PigStorage(',');
STORE conteo_fecha INTO 'salida_local/por_fecha' USING PigStorage(',');
