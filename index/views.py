# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import staticfiles
from django.core.cache import cache
from logging import warning as warn


def index(request):
    title = u"AC的新衣"
    dayHot = cache.get('dayHot')
    weekHot = cache.get('weekHot')
    monthHot = cache.get('monthHot')
    articleHot = cache.get('articleHot')
    hotArticle = []
    articles = []
    # get cached lastest commented articles
    cachedArticles = cache.get("getlastfeedback")

    # fake data
    toShow = 30
    if not cachedArticles:
        for i in xrange(toShow):
            item = {}
            item['link'] = "http://www.acfun.tv";
            item['title'] = u"【P.A. 奥妮】最炫过山风NL过山车X最炫民"
            item['desc'] = u"代投：农业重金属摇滚果然厉害！自带抗眩晕和提神BUFF！这次是同步率爆表的超同步最炫民族风过山车！奥妮表示以后困倦的时候就看这个提神了~欢迎大家多多吐槽~"
            item['image'] = "http://www.acfun.tv/r/cms/www/no_picture.gif"
            articles.append(item)
    # real data:
    else:
        toShow = len(articles)
        for k,v in cachedArticles.iteritems():
            if cache.get('preview'+str(v['id'])):
                v['image'] = cache.get('preview'+str(v['id']))
            else:
                v['image'] = "http://www.acfun.tv/r/cms/www/no_picture.gif"
            v['link'] = "http://www.acfun.tv/"+v['link']
            articles.append(v)

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))
