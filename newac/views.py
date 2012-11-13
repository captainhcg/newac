from models import *
from lib.ipinfodb import IPInfo

from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from django.db.models import Q
from django.template import RequestContext
from datetime import datetime, timedelta

import settings

# Create your views here.
def index(request):
    if request.visitor:
        return redirect("/guest/")
    ages = range(16, 61)
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def coming(request):
    visitor = Visitor()
    visitor.nickname 	= request.POST['nickname']
    visitor.age 		= request.POST['age']
    visitor.ip_address 	= request.remoteAddr
    visitor.visit_date 	= datetime.today()
    if visitor.ip_address == '127.0.0.1':
        visitor.ip_address = '61.174.51.1'

    dups = Visitor.objects.filter(ip_address = visitor.ip_address, nickname = visitor.nickname, visit_date = visitor.visit_date, age = visitor.age).order_by('-created_at')
    # if there is a very similar visitor, do not create new
    if dups:
        visitor = dups[0]
    else:
        visitor.save()
        try:
            ip_map = IPMap.objects.get(ip_address=visitor.ip_address)
        except:
            ip_map = IPMap()
        try:
            # retieve geo info
            # we shall always try if rely on 3rd party service
            ip_info = IPInfo()
            ip_map.createMapFromInfo(ip_info.GetIPInfo(visitor.ip_address))
            ip_map.save()
            visitor.ip_map = ip_map
            visitor.save()
        except:
            if settings.DEBUG:
                print "ERROR: Failed to retrieve geo info if ip %s for visitor %s" % (visitor.ip_address, visitor.id)
 
    request.session['visitor'] = visitor
    return redirect("/guest/") 

def leave(request):
    request.session['visitor'] = None
    return redirect("/")

def guest(request):
    try:
        visitor = request.visitor
        ip_map = visitor.ip_map
    except:
        return redirect("/")
    googlemap_apikey = settings.GOOGLEMAP_APIKEY
    birth_year = datetime.today().year - int(visitor.age)
    university_year =  min(datetime.today().year, birth_year + 18)
    return render_to_response('guest.html', locals(), context_instance=RequestContext(request))
