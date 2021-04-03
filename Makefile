
ifneq (,$(wildcard ./.env))
    include .env
    export
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

statics:
	python manage.py collectstatic


deploy-dev:
	rm .env
	sls deploy --stage dev --region us-east-2

deploy-prod:
	sls deploy --stage prod --region us-west-2