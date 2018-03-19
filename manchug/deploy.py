"""
WSGI config for manchug project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
from whitenoise.django import DjangoWhiteNoise


from django.core.wsgi import get_wsgi_application


path = "/home/AlvinAbaho/manchug/manchug"

if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manchug.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

