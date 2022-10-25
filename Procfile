heroku config:set DISABLE_COLLECTSTATIC=1
web: gunicorn ecommerce_backend.wsgi --log-file -
release: python manage.py makemigrations authentication
release: python manage.py migrate --noinput