# Куда пойти — Афиша Событий

![sample text](https://github.com/devmanorg/where-to-go-frontend/blob/master/.gitbook/assets/site.png?raw=true)

Интерактивная карта Москвы, на которой будут все известные виды активного отдыха с подробными описаниями и комментариями. Яндекс.Афиша занимается чем-то похожим, но это бездушный робот, собирающий всё подряд. Она никогда не обратит внимание на красивый канализационный люк или отвратительную вывеску.

## Установка проекта

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub.
```
git clone https://github.com/IsaUgurchiev/where_to_go.git
```

Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python3 manage.py migrate
```

Запустите сервер

```
python3 manage.py runserver
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

### Запустите проект:
```
python manage.py runserver 8000
```
Откройте сайт в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Загрузка данных
Чтобы загузить данные о месте выполните команду:
```
python manage.py load_place http://адрес/файла.json
```
#### Примеры файлов с данными доступны по ссылке: [Данные](https://github.com/devmanorg/where-to-go-places/tree/master)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

### Демо
Ссылка на демо версию - [https://isaugurchiev.pythonanywhere.com/](https://isaugurchiev.pythonanywhere.com/)