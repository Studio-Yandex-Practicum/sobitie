#!/bin/bash

docker-compose up -d --build
docker-compose exec web python drf_sobitie/manage.py makemigrations
docker-compose exec web python drf_sobitie/manage.py migrate --no-input
docker-compose exec web python drf_sobitie/manage.py collectstatic --no-input