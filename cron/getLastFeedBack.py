#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# enable debugging
from xml.dom.minidom import parseString
from HTMLParser import HTMLParser
import core, json

def update_list(ls):
    new_feeds = core.grabPage("www.acfun.tv", "/api/getlastfeedback.aspx");
    if new_feeds:
        new_feeds_list = json.loads(new_feeds)
    else:
        return

    for new_feed in new_feeds_list['feedbacks']:
        item = {}
        item['title'] = new_feed['title']
        item['desc'] = new_feed['description']
        item['link'] = new_feed['contentURL']
        item['id'] = new_feed['aid']
        item['time'] = int(new_feed['feedbackTime'])
        ls[item['id']] = item
        print item

    ls.sort(ls, key=lambda x: x['time'], reverse=True)
    print ls
    return

def main():
    memc = core.getMemc()
    if memc.get("getlastfeedback"):
        last_articles = memc.get("getlastfeedback")
    else:
        last_articles = {}
    update_list(last_articles)

if __name__ == "__main__":
    main()

