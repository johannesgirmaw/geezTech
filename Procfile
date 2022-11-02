heroku config:set DISABLE_COLLECTSTATIC=1
web: gunicorn elearning_backend.wsgi --log-file -
release: python manage.py makemigrations authentication
release: python manage.py migrate --noinput