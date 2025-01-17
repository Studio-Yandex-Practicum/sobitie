# Telegram бот для НКО "Событие"
## Оглавление
  - [Описание](#описание)
  - [Технологии](#технологии)
  - [Начало работы](#начало-работы)
    - [Подготовка к запуску](#подготовка-к-запуску)
    - [Запуск](#запуск)
    - [Запуск в контейнерах Docker-compose на сервере](#запуск-в-контейнерах-docker-compose-на-сервере)
    - [CI-CD](#ci-cd)
  - [Авторы](#авторы)
## Описание
Telegram бот для Центра социокультурных практик «Событие» помогает узнать подробнее о проектах организации, о людях состоящих в этом творческом содружестве, а также другую полезную информацию: контакты, как помочь, актуальные мероприятия и др. Пользователи могут подписаться на новые мероприятия и поиграть в квизы. 
## Технологии
- `python-telegram-bot` - Асинхронный интерфейс для Telegram Bot API. На нём реализован бот.
- `Django` - Используется для предоставления админ-панели для управления БД: квизами, вопросами, ответами и отправки уведомлений пользователям о новом мероприятии.

## Начало работы
### Подготовка к запуску
- Клонировать репозиторий проекта
```BASH
git clone git@github.com:Studio-Yandex-Practicum/sobitie.git
```
- Создайте .env
```BASH
cp .env-example .env
```
- Для генерации секретного ключа Django, запустите python скрипт `create_dj_secret_key.py`. Добавьте его в .env
```BASH
python create_dj_secret_key.py
```
- Установить зависимости
```BASH
pip install requirements.txt
```
- Выполнить миграции Django
```BASH
python drf_sobitie/manage.py migrate
```
##### Создание Telegram bot
- Вам понадобится Telegram бот <[Интерфейс для создания](https://telegram.me/BotFather)>  <[Туториал](https://core.telegram.org/bots/tutorial#obtain-your-bot-token)>
- Токент бота добавить в .env
##### Создать группу в vk
- ID группы добавить в .env
- Включите Long Poll API: Управление -> Работа с API -> Long Poll API -> Включить
- Подключите необходимые события: ... -> Long Poll API -> Типы событий  -> Записи на стене -> Добавление
##### Создать приложение в vk
- [Интерфейс создания приложения](https://vk.com/apps?act=manage)
- Скопируйте сервисный токен из настроек приложения и добавьте его в .env
- [Создайте токен доступа](https://dev.vk.com/ru/api/access-token/implicit-flow-community#Открытие%20диалога%20авторизации). Дополните запрос ниже, вставьте его в адресную строку браузера, разрешите доступ. Скопируйте токен доступа из адресной строки браузера "...access_token_223361982=<сервисный токен>"
```
https://oauth.vk.com/authorize
?client_id=<ID вашего vk приложения>
&group_ids=<ID вашей vk группы>
&display=page
&redirect_uri=https://oauth.vk.com/blank.html
&scope=wall,manage
&response_type=token
&v=5.131
```
- Токен доступа добавить в .env

### Запуск
- Запуск Django
```
python drf_sobitie/manage.py runserver
```
- Запуск Бота
```
python manage.py runbot
```
*** Для более удобного развертывания рекомендуем запуск через docker compose

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
или `run_local.sh` для локального запуска
```BASH
./run_local.sh
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
- [Варламов Антон](https://github.com/Todvaa)
