
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

runserver:
	python manage.py runserver

migrate:
	echo $(DB_NAME)
	python manage.py migrate api $(params)

showmigrations:
	python manage.py showmigrations api

makemigrations:
	python manage.py makemigrations api

createsuperuser:
	python manage.py createsuperuser

statics:
	python manage.py collectstatic