# Telegram бот для НКО "Событие"
## Оглавление
1. [Описание](https://github.com/Studio-Yandex-Practicum/sobitie#описание)
2. [Технологии](https://github.com/Studio-Yandex-Practicum/sobitie#технологии)
3. [Начало работы](https://github.com/Studio-Yandex-Practicum/sobitie#начало-работы)
    1. [Требования](https://github.com/Studio-Yandex-Practicum/sobitie#требования)
    2. [Запуск в контейнерах Docker-compose на сервере](https://github.com/Studio-Yandex-Practicum/sobitie#запуск-в-контейнерах-docker-compose-на-сервере)
    3. [Запуск в режиме разработчика](https://github.com/Studio-Yandex-Practicum/sobitie#запуск-в-режиме-разработчика)
4. [Авторы](https://github.com/Studio-Yandex-Practicum/sobitie#авторы)
## Описание
Telegram бот для Центра социокультурных практик «Событие» помогает узнать подробнее о проектах организации, о людях состоящих в этом творческом содружестве, а также другую полезную информацию: контакты, как помочь, актуальные мероприятия и др. Пользователи могут подписаться на новые мероприятия и поиграть в квизы. 
## Технологии
- `python-telegram-bot` - Асинхронный интерфейс для Telegram Bot API. На нём реализован бот.
- `Django` - Используется для предоставления админ-панели для управления БД: квизами, вопросами и ответами.
- `FastAPI` - Используется принятия HTTP-запросов от Django приложения ботом. В частости, для отправки уведомлений пользователям о новом мероприятии.
## Начало работы
### Требования
- Вам понадобится Telegram бот и токен к нему (см. [туториал](https://core.telegram.org/bots/tutorial#obtain-your-bot-token))
- [Сервисный ключ](https://vk.com/faq11759) доступа приложения VK 
### Запуск в контейнерах Docker-compose на сервере
1. Клонировать репозиторий проекта
```BASH
git clone git@github.com:Studio-Yandex-Practicum/sobitie.git
```
2. Перейти в корневую папку проекта 
```BASH
cd sobitie/
```
3. Создать `.env` и заполнить пустые значения по образцу `.env-example`
```BASH
touch .env
nano .env
# Для сохранения файла используйте CTRL+O
# Если просит ввести имя файла, то проверьте правильность и подтвердите нажатием Enter
```
- Чтобы сгенерировать секретный ключ Django, запустите python скрипт `create_dj_secret_key.py`
```BASH
python create_dj_secret_key.py
```
Далее скопируйте его и заполните нужную переменную в `.env`  
4. Запустить скрипт `run.sh`
```BASH
./run.sh
```
### Запуск в режиме разработчика
1. Клонировать репозиторий проекта
```BASH
git clone git@github.com:Studio-Yandex-Practicum/sobitie.git
```
2. Перейти в корневую папку проекта
```BASH
cd sobitie/
```
3. Установить зависимости. Виртуальное окружение будет создано автоматически
```BASH
poetry install
```
4. Создать `.env` и заполнить его по образцу `.env-example`
- Чтобы сгенерировать секретный ключ Django, запустите python скрипт `create_dj_secret_key.py`
```BASH
python create_dj_secret_key.py
```
- При запуске не в контейнерах придётся скорректировать URL`ы
5. Выполнить миграции Django
```BASH
python drf_sobitie/manage.py migrate
```
6. Создать администратора Django
```BASH
python drf_sobitie/manage.py createsuperuser
# Следовать указаниям в терминале
```
7. Запустить приложения
```BASH
python drf_sobitie/manage.py runserver
# Открыть новый терминал, перейти в корневую директорию проекта
python src/main.py 
# Открыть новый терминал, перейти в корневую директорию проекта
cd src/
uvicorn fastapi_app:fastapi_app --port <незанятый порт>
# Напоминаю, что в .env-example были приведены ссылки для запуска бота в контейнерах, поэтому в .env их следовало скорректировать
```
### CI-CD
- залить файл docker-compose на сервер в домашнюю директорию
- залить каталог nginx на сервер в домашнюю директорию

```
sudo apt update && apt upgrade
sudo apt install docker-compose
```

## Авторы 
- [Бойко Владислав](https://github.com/bdwayne11)
- [Кирилл Резник](https://github.com/Invictus-7)
- [Екатерина Каричева](https://github.com/kh199)
- [Никита Цыбин](https://github.com/kellia1903)
- [Артём Ултанов](https://github.com/WayBro-54)
- [Даниил Паутов](https://github.com/TomatoInOil)
- [Владимир Тихий](https://github.com/vladimirramozin)
- [Вячеслав Роев](https://github.com/VyacheslavRoev)
- [Оксана Шеремет](https://github.com/sheremet-o)
- [Сергей Разуваев](https://github.com/RazuvaevSD)
- [Мясищев Максим](https://github.com/mnmyasis)
