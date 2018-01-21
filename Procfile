release: python manage.py migrate --settings=config.heroku
web: gunicorn config.wsgi --log-file -
