# UTCC motor parking
🛵 🛵 🛵 🛵 🛵 🛵 🛵 🛵 🛵 🛵 🛵 🛵

## Setup Project (First time only)
Build docker images
    ```bash
    docker-compose build --no-cache
    ```

## Run Project
1. Start Database
    ```bash
    docker-compose up db
    ```
2. Start Django
    ```bash
    docker-compose up web
    ```
   
#### Run makemigrations
```bash
docker-compose exec web python manage.py makemigrations
```
#### Run migrate
```bash
docker-compose exec web python manage.py migrate
```
#### Run startapp
```bash
docker-compose exec web python manage.py startapp <appname>
```

## Technologies
- Python 3.8.0
- Django 3.1.0
- Postgres 12.4