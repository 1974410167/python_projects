"""
WSGI config for DRF project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF.settings')
# def get_wsgi_application():
#     django.setup(set_prefix=False)
#     return WSGIHandler()

application = get_wsgi_application()
