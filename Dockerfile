# docker run -v $(pwd):/app -p 8000:8000 -w /app python:3.9 bash -c "pip install -r requirements.txt && python manage.py runserver 0.0.0.0:8000"
FROM python:3.9
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
