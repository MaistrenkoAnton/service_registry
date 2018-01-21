import dj_database_url

try:
    from config.settings import *
except ImportError:
    pass

ALLOWED_HOSTS = ['*']
DEBUG = False

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES = dict(default={})
DATABASES['default'].update(db_from_env)
