FROM python:3.11

# Instalar Java 17 y herramientas necesarias para Pig
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk wget curl bash unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))" >> /etc/profile.d/java_home.sh && \
    echo "export PATH=\$JAVA_HOME/bin:\$PATH" >> /etc/profile.d/java_home.sh

# Instalar Apache Pig
RUN wget https://downloads.apache.org/pig/pig-0.17.0/pig-0.17.0.tar.gz && \
    tar -xvzf pig-0.17.0.tar.gz && \
    mv pig-0.17.0 /opt/pig && \
    rm pig-0.17.0.tar.gz && \
    echo "export PIG_HOME=/opt/pig" >> /etc/profile.d/pig_home.sh && \
    echo "export PATH=\$PIG_HOME/bin:\$PATH" >> /etc/profile.d/pig_home.sh


# Variables de entorno para Java y Pig
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PIG_HOME=/opt/pig
ENV PATH="$PIG_HOME/bin:$PATH"

# Crear directorio de trabajo
WORKDIR /app

# Copiar todos los archivos del proyecto
COPY . /app

# Instalar dependencias Python
RUN pip install --no-cache-dir pymongo cachetools numpy pandas matplotlib seaborn scikit-learn

# Agregar script final que automatiza Python + Pig + copia CSV
COPY post_pipeline.sh /app/post_pipeline.sh
RUN chmod +x /app/post_pipeline.sh

# Ejecutar automáticamente todo el flujo
CMD ["bash", "/app/post_pipeline.sh"]
