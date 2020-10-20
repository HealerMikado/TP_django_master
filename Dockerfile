# Téléchargement de la dernière image python
FROM python:3.8.3-alpine

# Création de variable d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installation de package nécessaire à lxml
RUN apk add --no-cache --virtual .build-deps gcc libc-dev libxslt-dev && \
    apk add --no-cache libxslt && \
    pip install --no-cache-dir lxml>=3.5.0 && \
    apk del .build-deps


ADD . .


# installation du fichier requirements.txt
RUN pip install -r requirements.txt




# Run l'application
CMD python manage.py makemigrations;python manage.py migrate;gunicorn mysite.wsgi -b 0.0.0.0:8000

