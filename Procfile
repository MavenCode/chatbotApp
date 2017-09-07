web:python manage.py runserver
web: gunicorn uploads.wsgi --log-file -
heroku ps:scale web=1
