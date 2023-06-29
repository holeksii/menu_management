#!/bin/bash
echo "Starting Migrations..."
python3 manage.py migrate
echo ====================================

env $(cat api.env | xargs) rails

echo "Starting Server..."
echo "PORT = ${API_PORT}"
python3 manage.py runserver ${API_PORT}
