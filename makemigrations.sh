source ../../env/bin/activate
read -p 'python manage.py makemigrations app:' app

python manage.py makemigrations $app
python manage.py migrate