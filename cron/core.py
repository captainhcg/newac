# coding=utf-8
import httplib
import mysql.connector as mdb
from django.core.cache import cache

def grabPage( site, page ):
    try:
        httpconn = httplib.HTTPConnection(site)
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        httpconn.request("GET", page, headers = headers)
        resp = httpconn.getresponse()
        resppage = resp.read()
    except:
        resppage = ""
    return resppage
