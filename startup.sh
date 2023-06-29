#!/bin/bash

python3 manage.py waitfordb

echo "Starting Migrations..."
python3 manage.py migrate
echo ====================================

echo "Starting Server..."
echo "PORT = ${API_PORT}"
python3 manage.py runserver ${API_PORT}
