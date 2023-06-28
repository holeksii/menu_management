FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# EXPOSE 8000:8000

ENTRYPOINT ["./startup.sh"]

# ENTRYPOINT ["python3", "manage.py" ,"runserver"]
