source ../../env/bin/activate
read -p 'python manage.py sqlmigrate chapters 0001_initial:' app_label  migration_name

python manage.py sqlmigrate $app_label $migration_name
