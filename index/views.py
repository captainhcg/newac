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
    topShow = 16
    for i in xrange(topShow):
        item = {}
        item['name'] = str(random.randint(100, 999))
        dayHot.append(item)

    for i in xrange(topShow):
        item = {}
        item['name'] = str(random.randint(100, 999))
        weekHot.append(item)

    for i in xrange(topShow):
        item = {}
        item['name'] = str(random.randint(100, 999))
        monthHot.append(item)

    for i in xrange(topShow):
        item = {}
        item['name'] = str(random.randint(100, 999))
        hotArticle.append(item)

    toShow = 30
    articles = []
    for i in xrange(toShow):
        item = {}
        item['link'] = "http://www.acfun.tv";
        item['title'] = u"【P.A. 奥妮】最炫过山风NL过山车X最炫民"
        item['description'] = u"代投：农业重金属摇滚果然厉害！自带抗眩晕和提神BUFF！这次是同步率爆表的超同步最炫民族风过山车！奥妮表示以后困倦的时候就看这个提神了~欢迎大家多多吐槽~"
        item['image'] = "http://www.acfun.tv/r/cms/www/no_picture.gif"
        articles.append(item)

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))
