Телеграмм-бот для НКО "Событие"

Что сделал 19.02.2023 (Кирилл)

- создал меню "Помочь" и 8 кнопок к нему;
- активировал 2 кнопки в этом меню - "Пожертвования" и "Прийти на спектакль" - сейчас они
возвращают простое текстовое сообщение от бота;
- реализовал функцию возврата назад на главную страницу из меню "Помочь";
- вынес кнопки и настройки все меню в constants.py;
- переименовал возвращаемые функциями состояния в единообразный вид с суффиксом STATE -
теперь у нас имеются START_STATE, ABOUT_US_STATE, SUPPORT_STATE
- начал добавлять эмотиконы к кнопкам (дополнил окружение библиотекой emoji)
