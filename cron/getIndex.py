#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# enable debugging
from xml.dom.minidom import parseString
from core import cache, grabPage
import re

def getHotData(data):
    inf = {}
    inf['link'] = re.findall('(?<=href=").*?(?=" )', data, re.S)[0]
    inf['preview'] = re.findall('(?<=data-preview=").*?(?=" )', data, re.S)[0]
    inf['title'] = re.findall('(?<=data-title=").*?(?=" )', data, re.S)[0]
    inf['data-desc'] = re.findall('(?<=data-desc=").*?(?=" )', data, re.S)[0]
    inf['id'] = re.findall('\d+',inf['link'])[0]
    if inf['preview'].find('no_picture.gif') == -1:
        cache.set("preview"+inf['id'], inf['preview'])
    # inf['data-author'] = re.findall('(?<=data-author=").*?(?=" )', data)
    return inf

def processHot(data):
    day_hot = re.findall('<!--周排行开始-->.*?<!--周排行结束-->', data, re.S)[0]
    week_hot = re.findall('<!--月排行开始-->.*?<!--月排行结束-->', data, re.S)[0]
    article_hot = re.findall('<!--文章区列表开始-->.*?<!--文章区列表结束-->', data, re.S)[0]

    day_hot_list = []
    week_hot_list = []
    article_hot_list = []
    if day_hot:
        day_list = re.findall('<a.*?</a>', day_hot)
        for item in day_list:
            day_hot_list.append(getHotData(item))
        cache.set('dayHot', day_hot_list, 3600*24)

    if week_hot:
        week_list = re.findall('<a.*?</a>', week_hot)
        for item in week_list:
            week_hot_list.append(getHotData(item))
        cache.set('weekHot', week_hot_list, 3600*24)

    if article_hot:
        article_list = re.findall('<a.*?</a>', article_hot)
        for item in article_list:
            article_hot_list.append(getHotData(item))
        cache.set('articleHot', article_hot_list, 3600*24)
            

def main():
    try:
        data = grabPage("www.acfun.tv", "")
        processHot(data)
    except:
        pass

if __name__ == "__main__":
    main()
