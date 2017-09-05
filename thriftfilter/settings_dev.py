"""
This file will override the settings in settings.py if a DJANGO_DEVELOPMENT env variable is set.
On the computer that will be used for development, add this to your ~/.bashrc file:
export DJANGO_DEVELOPMENT = true
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG = True

# This should not be necessary unless there are database environment variables 
# set in the same manner as Heroku
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}