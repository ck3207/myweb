#!encoding:utf-8
import logging

from django.conf import settings

logging.basicConfig(filename=settings.LOG_FILE, level=settings.LOG_LEVEL, 
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filemode='a'
                )

