from django.test import TestCase

# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myweb.settings") # project_name 项目名称
# django.setup()

# from django.db.models import ConfigTable
# from utilities.data_from_database import update
# Create your tests here.

# update(ConfigTable, section='public', option='light')
from log import logging

        
logging.info('Im in tests file.')