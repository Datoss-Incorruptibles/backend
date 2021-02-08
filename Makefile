config-local:
	DB_HOST=localhost
	DB_NAME=elecciones
	DB_USER=develop
	DB_PASSWORD=develop
	DB_PORT=5433
	SECRET_KEY="e_(x5@3t65y996!ch$m*uf6y3j1a8zeh$h4=uiktp0c9oarkla"
	DEBUG=True

run-local:
	make config-local
	python manage.py runserver

migrate-local:
	make config-local
	python manage.py makemigrations
	python manage.py migrate api $(params)

showmigrations-local:
	make config-local
	python manage.py showmigrations api


config-dev:
	DB_HOST=datosincorruptibles.c6gg6kroo2es.us-east-2.rds.amazonaws.com
	DB_NAME=elecciones2021
	DB_USER=roleA
	DB_PASSWORD=B8HNzDwS1WEWjf
	SECRET_KEY='e_(x5@3t65y996!ch$m*uf6y3j1a8zeh$h4=uiktp0c9oarkla'
	DB_PORT=5432

migrate-dev:
	make config-dev
	python manage.py makemigrations
	python manage.py migrate api $(params)

showmigrations-dev:
	make config-dev
	python manage.py showmigrations api


createsuperuser-dev:
	make config-dev
	python manage.py createsuperuser