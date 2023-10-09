#!/bin/bash

docker-compose up -d --build
docker-compose exec web python drf_sobitie/manage.py makemigrations event
docker-compose exec web python drf_sobitie/manage.py makemigrations quiz
docker-compose exec web python drf_sobitie/manage.py makemigrations sticker_pack
docker-compose exec web python drf_sobitie/manage.py migrate --no-input
docker-compose exec web python drf_sobitie/manage.py collectstatic --no-input
docker-compose exec bot python drf_sobitie/manage.py makemigrations event
docker-compose exec bot python drf_sobitie/manage.py makemigrations quiz
docker-compose exec bot python drf_sobitie/manage.py makemigrations sticker_pack
docker-compose exec bot python drf_sobitie/manage.py migrate --no-input
docker-compose exec bot python drf_sobitie/manage.py collectstatic --no-input