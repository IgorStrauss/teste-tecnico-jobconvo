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
	coverage run project-jobconvo/manage.py test


makemigrations:
	python project-jobconvo/manage.py makemigrations

migrate:
	python project-jobconvo/manage.py migrate