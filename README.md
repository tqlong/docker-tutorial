## Cài đặt Docker
Sử dụng: https://www.docker.com/get-started/

## Run MariaDB server
```bash
docker run -d --name mariadb -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 mariadb

docker exec -it mariadb /bin/bash

mariadb -u root -p
```

Vào trong MariaDB server và sử dụng các lệnh SQL như đã học.

## Create Django project
```bash
docker run -v $(pwd):/app -w /app python:3.9 bash -c "pip install django && django-admin startproject mysite ."

docker run -v $(pwd):/app -p 8000:8000 -w /app python:3.9 bash -c "pip install -r requirements.txt && python manage.py runserver 0.0.0.0:8000"
```

## Viết Dockerfile thay thế cho câu lệnh trên
```Dockerfile
FROM python:3.9
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## Create Django image with Dockerfile
```bash
docker build -t django-example .

docker run -p 8000:8000 django-example
```

Xem trang web tại: http://localhost:8000

## Sử dụng DockerHub
- Cài đặt một image bất kì từ DockerHub
- Đẩy image bạn vừa tạo lên DockerHub