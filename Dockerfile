# Usa una imagen oficial de Python como imagen base
FROM python:3.10-slim

# Agrega un usuario no root
RUN useradd -m myuser

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos actuales del directorio al contenedor en /app
COPY . /app

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Cambia al usuario no root
USER myuser

# Expone el puerto 5000 para acceder desde fuera del contenedor
EXPOSE 5000

# Instala Gunicorn
RUN pip install gunicorn

# Ejecuta Gunicorn cuando se lance el contenedor
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
