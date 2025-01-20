#!/bin/bash

docker-compose -f docker-compose_local.yaml up --build
# docker-compose -f docker-compose_local.yaml up -d --build
docker-compose -f docker-compose_local.yaml exec web python manage.py makemigrations
docker-compose -f docker-compose_local.yaml exec web python manage.py migrate --no-input
docker-compose -f docker-compose_local.yaml exec web python manage.py collectstatic --no-input
