#!/bin/bash
cd testdjangoapp
python manage.py collectstatic
gunicorn -c gunicorn_config.py testdjangoapp.wsgi