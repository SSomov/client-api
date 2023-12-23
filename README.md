##Установка poetry
```
https://python-poetry.org/docs/#installing-with-the-official-installer
```
##Установка зависимостей
```
poetry install
```
##Настройка credentials.json

Создать файл _.env_ в корне проекта и добавить в него
```
URL_API = "https://example.io/api/v1/"
EMAIL=your_email
PASSWORD=your_password
```
##Использование
```
poetry run python main.py
```