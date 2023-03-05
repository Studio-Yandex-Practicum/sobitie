# Телеграмм-бот для НКО "Событие"

## В данной реализации бота будет использоваться следующая архитектура:

```
* Основная логика в папке src, библиотека python-telegram-bot.
* К боту так же подключена django-rest-framework. 
```

### Основные урлы:
```
http://127.0.0.1:8000/api/categories/ - для всех категорий событий
http://127.0.0.1:8000/api/events/ - для всех событий
http://127.0.0.1:8000/api/quotes/ - для всех цитат
```

## Запустить бота + api можно:
### Склонировав себе репозиторий:

```
git clone git@github.com:Studio-Yandex-Practicum/sobitie.git
```

### Установить зависимости:

```
poetry install
```

### Создать .env

```
TELEGRAM_TOKEN=your_token
DJ_SECRET_KEY=your_secret_key
```

### Сделать миграции:

```
cd drf_sobitie/
python manage.py migrate
```

### Запуск api + bot: 
```
python manage.py runserver
открыть еще один терминал
cd src/
python main.py
```

## Team: 
 * bdwayne11 Бойко Владислав
 * Invictus-7 Кирилл Резник
 * kh199 Екатерина Каричева
 * kellia1903 Никита Цыбин
 * WayBro-54 Артём 
