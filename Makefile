# bin/sh

start:
	python project-jobconvo/manage.py makemigrations
	python project-jobconvo/manage.py migrate
	python project-jobconvo/manage.py runserver 

run:
	python project-jobconvo/manage.py runserver

test:
	python project-jobconvo/manage.py test

pytest:
	pytest

coverage:
	pytest --cov=. --cov-report=html --cov-report

makemigrations:
	python project-jobconvo/manage.py makemigrations

migrate:
	python project-jobconvo/manage.py migrate