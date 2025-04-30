import numpy as np
import random

def generar_consultas(ids_eventos, n_consultas, distribucion, lambda_poisson, p_binomial):
    if distribucion == "poisson":
        indices = np.random.poisson(lam=lambda_poisson, size=n_consultas)
    elif distribucion == "binomial":
        indices = np.random.binomial(n=len(ids_eventos)-1, p=p_binomial, size=n_consultas)
    else:
        raise ValueError("Distribución no válida: usa 'poisson' o 'binomial'.")

    consultas = [{"id": int(i) % len(ids_eventos)} for i in indices]
    random.shuffle(consultas)
    return consultas
