#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# enable debugging
from xml.dom.minidom import parseString
from HTMLParser import HTMLParser
from core import cache, grabPage

class indexHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            try:
                if attrs['id'] == "tabbable-index-rank":
                    print "asd"
                    print self.get_starttag_text()
            except:
                pass
        
def main():
    parser = indexHTMLParser()
    parser.feed(grabPage("www.acfun.tv", "").decode("utf-8"))
    
if __name__ == "__main__":
    main()
