from __future__ import unicode_literals

import django
from django.conf import settings
from django.core.management import call_command

settings.configure(
    INSTALLED_APPS=('robokassa',),
    DATABASE_ENGINE='sqlite3',
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        },
    },

    ROBOKASSA_LOGIN='Chitalocka',
    ROBOKASSA_PASSWORD1='password4543',
    ROBOKASSA_PASSWORD2='password4545',
    ROBOKASSA_EXTRA_PARAMS=['param1', 'param2'],
)

django.setup()

if __name__ == "__main__":
    call_command('test', 'robokassa')
