from cachetools import LRUCache, LFUCache

def crear_cache(politica, tamano):
    if politica.upper() == "LRU":
        return LRUCache(maxsize=tamano)
    elif politica.upper() == "LFU":
        return LFUCache(maxsize=tamano)
    else:
        raise ValueError("Política de caché no válida. Usa 'LRU' o 'LFU'.")
