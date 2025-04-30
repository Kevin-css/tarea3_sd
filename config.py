# Cantidad fija de eventos simulados
N_EVENTOS = 10000

# Combinaciones a evaluar automáticamente
CONFIGS_EVALUACION = {
    "n_consultas": [500, 1000, 3000, 5000],
    "cache_policies": ["LRU", "LFU"],
    "cache_sizes": [50, 200, 500, 1500],
    "distribuciones": ["poisson", "binomial"]
}

# Parámetros por distribución
LAMBDA_POISSON = 1    
P_BINOMIAL = 0.5        