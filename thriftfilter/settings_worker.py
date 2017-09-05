"""
This file will override the settings in settings.py if a DJANGO_WORKER env variable is set.
On the computer that will be used for development, add this to your ~/.bashrc file:
export DJANGO_WORKER = true

Make sure that DB_URL is set to the database url provided by heroku as well
export DB_URL = [database url]
"""
import os

DEBUG = True

import dj_database_url
DATABASES = {'default': dj_database_url.config(default=os.environ.get('DB_URL'), conn_max_age=500)}