# Тестовое задание

Приложение для бронирования комнат в отеле

### Требования:
* Для комнат должны быть поля: номер/название, стоимость за сутки, количество мест.
* Пользователи должны уметь фильтровать и сортировать комнаты по цене, по количеству мест.
* Пользователи должны уметь искать свободные комнаты в заданном временном интервале.
* Пользователи должны уметь забронировать свободную комнату.
* Суперюзер должен уметь добавлять/удалять/редактировать комнаты и
редактировать записи о бронях через админ панель Django.
* Брони могут быть отменены как самим юзером, так и суперюзером.
* Пользователи должны уметь регистрироваться и авторизовываться (логиниться).
* Чтобы забронировать комнату пользователи должны быть авторизованными.
Просматривать комнаты можно без логина.
Авторизованные пользователи должны видеть свои брони.

Стек:
* Django;
* DRF;
* СУБД предпочтительно PostgreSQL, но не обязательно. Главное не SQLite;
* При необходимости можно добавлять другие библиотеки.

Приветствуется:
* Автотесты;
* Аннотации типов;
* Линтер;
* Автоформатирование кода;
* Документация к API;
* Инструкция по запуску приложения.

## Страницы
* .../rooms/ - Страница всех комнат
* .../rooms/<room_id> - Страница информации конкретной комнаты
* .../booked_dates/ - Страница со всеми забронированными датами пользователя
* .../booked_dates/delete/<booking_records_id> - Ручка для удаления брони.


* .../login/ - Страница авторизации
* .../register/ - Страница регистрации
* .../logout/ - Страница выхода

# Инструкция по запуску
Для запуска приложения вам необходим docker и docker-compose
1. Заполнить конфиги.
Для этого необходимо создать файл .env в корневой директории проекта и заполнить его как в .env_example.
2. Собрать проект командой
```commandline
docker-compose build
```
3. Запустить проект командой
```commandline
docker-compose up
```
4. Создать суперпользователя командой
```commandline
docker exec -it django python manage.py createsuperuser
```
Ваше приложение запущено.
