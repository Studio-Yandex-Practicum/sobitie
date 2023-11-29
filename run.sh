#!/bin/bash

docker-compose up -d --build
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate --no-input
docker-compose exec web python manage.py collectstatic --no-input