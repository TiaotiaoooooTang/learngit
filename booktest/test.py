from django.test import TestCase
import os
from demo.demo import settings

# Create your tests here.
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

import django
django.setup()
# from .models import BookInfo, HeroInfo
from .models import BookInfo , HeroInfo


if __name__ == '__main__':
    print(BookInfo)
