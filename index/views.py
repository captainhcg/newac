# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import staticfiles


def index(request):
    title = u"AC的新衣"
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))