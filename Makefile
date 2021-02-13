
ifeq ($(env), dev)
export DB_HOST=datosincorruptibles.c6gg6kroo2es.us-east-2.rds.amazonaws.com
export DB_NAME=elecciones2021
export DB_USER=roleA
export DB_PASSWORD=B8HNzDwS1WEWjf
export SECRET_KEY="e_(x5@3t65y996!ch$m*uf6y3j1a8zeh$h4=uiktp0c9oarkla"
export DB_PORT=5432
else
export DB_HOST=localhost
export DB_NAME=elecciones
export DB_USER=develop
export DB_PASSWORD=develop
export DB_PORT=5433
export SECRET_KEY="e_(x5@3t65y996!ch$m*uf6y3j1a8zeh$h4=uiktp0c9oarkla"
export DEBUG=True
endif 

runserver:
	python manage.py runserver

migrate:
	python manage.py migrate api $(params)

showmigrations:
	python manage.py showmigrations api

makemigrations:
	python manage.py makemigrations api

createsuperuser:
	python manage.py createsuperuser
