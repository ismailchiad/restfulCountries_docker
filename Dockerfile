#Je choisis une image "template" de python
FROM python:3.9

#je choisis un répertoire de travail
WORKDIR /code

#je copie les requirements de mon projet vers mon espace 
#de travail sur mon conteneur
COPY ./requirements.txt /code/requirements.txt

#je lance l'installation des bibliothèques sur mon conteneur
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#je copie le reste de mon projet situé dans app
COPY ./app /code/app

#je spécifie le command par defaut pour lancé le conteneur
CMD [ "fastapi","run","app/main.py","--port","80" ]