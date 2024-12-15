#!/bin/bash

docker-compose -f docker-compose-local.yaml up -d --build
docker-compose -f docker-compose-local.yaml exec web python manage.py makemigrations
docker-compose -f docker-compose-local.yaml exec web python manage.py migrate --no-input
docker-compose -f docker-compose-local.yaml exec web python manage.py collectstatic --no-input
