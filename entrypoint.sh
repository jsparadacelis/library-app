#!/bin/bash

echo "Waiting for db.."
python manage.py check --database default > /dev/null 2> /dev/null
until [ $? -eq 0 ];
do
  sleep 2
  python manage.py check --database default > /dev/null 2> /dev/null
done
echo "Connected."

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
