# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import staticfiles


def index(request):
    title = u"AC的新衣"
    dayHot = []
    weekHot = []
    monthHot = []
    hotArticle = []
    import random
    topShow = 15
    for i in range(1, topShow):
        item = {}
        item['name'] = str(random.randint(100, 999))
        dayHot.append(item)

    for i in range(1, topShow):
        item = {}
        item['name'] = str(random.randint(100, 999))
        weekHot.append(item)

    for i in range(1, topShow):
        item = {}
        item['name'] = str(random.randint(100, 999))
        monthHot.append(item)

    for i in range(1, topShow):
        item = {}
        item['name'] = str(random.randint(100, 999))
        hotArticle.append(item)

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))
