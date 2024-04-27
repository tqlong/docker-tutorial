## Run MariaDB server
```bash
docker run -d --name mariadb -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 mariadb

docker exec -it mariadb /bin/bash

mariadb -u root -p
```

## Create Django project
```bash
docker run -v $(pwd):/app -w /app python:3.9 bash -c "pip install django && django-admin startproject mysite ."

docker run -v $(pwd):/app -p 8000:8000 -w /app python:3.9 bash -c "pip install -r requirements.txt && python manage.py runserver 0.0.0.0:8000"
```

## Create Django image with Dockerfile
```bash
docker build -t django-example .

docker run -p 8000:8000 django-example
```
