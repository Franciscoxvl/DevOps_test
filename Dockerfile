# Usa una imagen base de Python 3.11
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt y lo instala
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY . .

# Expon el puerto que Gunicorn utilizará
EXPOSE 5000

# Comando para ejecutar la aplicación con Gunicorn
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "app:app"]
