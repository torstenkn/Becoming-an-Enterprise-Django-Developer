"""
Local Django settings for becoming_a_django_entdev project.

Based on by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e8a4a113-8637-41f4-be33-5c707fc9b3fc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1',
]

# Use this to configure a local PostgreSQL Database to use
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'database_name',
#        'HOST': 'localhost',
#        'USER': 'database_user',
#        'PASSWORD': 'database_password',
#        'PORT': '5432',
#    }
#}

