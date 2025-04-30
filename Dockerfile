# Dockerfile

FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar todos los archivos al contenedor
COPY . /app

# Instalar dependencias necesarias
RUN pip install --no-cache-dir pymongo cachetools numpy pandas matplotlib seaborn scikit-learn

# Comando por defecto al iniciar el contenedor
CMD ["python", "main.py"]
