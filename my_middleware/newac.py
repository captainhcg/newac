import re
import settings
import datetime
from django import http
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.sites.models import Site #Find current site (drchrono.com or localhost:8000)
from django.core.mail import send_mail
from django.utils import simplejson
from django.utils.datastructures import SortedDict
from django.utils.http import urlquote

# from wuhulu.models import *

class NewACMiddleware(object):
    def __init__(self):
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path.startswith(settings.STATIC_URL):
            return None
        if not request.user.is_authenticated():
            setattr(request, 'remoteAddr', request.META['REMOTE_ADDR'])
            try:
                request.visitor = request.session['visitor']
            except:
                request.visitor = None

