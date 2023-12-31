from burgarkartan.settings import *

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", None)
ALLOWED_DOMAINS = os.environ["ALLOWED_DOMAINS"].split(",")

X_FRAME_OPTIONS = 'SAMEORIGIN'

EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_SENDER = os.environ.get("EMAIL_SENDER")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True

DJANGO_POSTGRESQL_DBNAME = os.environ.get('POSTGRES_DB')
DJANGO_POSTGRESQL_USER = os.environ.get('POSTGRES_USER')
DJANGO_POSTGRESQL_PASS = os.environ.get('POSTGRES_PASSWORD')
DJANGO_POSTGRESQL_HOST = os.environ.get('POSTGRES_HOST')

ALLOWED_HOSTS = ALLOWED_DOMAINS
#INTERNAL_IPS = ['127.0.0.1']

CSRF_TRUSTED_ORIGINS = [
    'https://burgarkartan.se'
]

DEBUG = False
DJANGO_LOG_LEVEL = DEBUG
#MEDIA_ROOT = "/var/www/usercontent.burgarkartan.se/"
#MEDIA_URL = "/files/"
#STATIC_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DJANGO_POSTGRESQL_DBNAME,
        'USER': DJANGO_POSTGRESQL_USER,
        'PASSWORD': DJANGO_POSTGRESQL_PASS,
        'HOST': DJANGO_POSTGRESQL_HOST,
        'PORT': '5432',
        'OPTIONS': {

        },
    }
}
