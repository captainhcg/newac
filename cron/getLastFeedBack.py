#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# enable debugging
from xml.dom.minidom import parseString
from HTMLParser import HTMLParser
import core, json
from core import cache

def update_dict(dic):
    new_feeds = core.grabPage("www.acfun.tv", "/api/getlastfeedback.aspx")
    if new_feeds:
        new_feeds_list = json.loads(new_feeds)
    else:
        return

    for new_feed in new_feeds_list['feedbacks']:
        item = {}
        item['title'] = new_feed['title']
        try:
            item['desc'] = new_feed['description']
        except KeyError:
            item['desc'] = ""
        item['link'] = new_feed['contentURL']
        item['id'] = new_feed['aid']
        item['time'] = int(new_feed['feedbackTime'])
        dic[item['id']] = item

    items = []
    for k, v in dic.iteritems():
        items.append(v)
    
    items.sort(articleComparator)
    new_dict = {}

    count = 1;
    for item in items:
        new_dict[item['id']] = item
        if ++count > 100:
            break

    cache.set("getlastfeedback", new_dict, 3600*24)
    return

def articleComparator(i1, i2):
    if i2['time'] > i1['time']:
        return 1
    elif i2['time'] == i1['time']:
        return 0
    return -1

def main():
    if cache.get("getlastfeedback"):
        last_articles = cache.get("getlastfeedback")
    else:
        last_articles = {}
    update_dict(last_articles)

if __name__ == "__main__":
    main()

