#!/bin/bash
echo "Creating Migrations..."
python3 manage.py makemigrations menu_management_api/api
echo ====================================

echo "Starting Migrations..."
python3 manage.py migrate
echo ====================================

echo "Starting Server..."
python3 manage.py runserver
