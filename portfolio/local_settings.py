import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfoliodb',
        'USER':'postgres',
        'PASSWORD':'Ishan@Extreme',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

DEBUG = True