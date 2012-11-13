import settings, json, urllib, urllib2
class IPInfo() :
    def __init__(self) :
        self.apikey = settings.IPINFODB_APIKEY
        self.baseurl = "http://api.ipinfodb.com/v3/ip-city/"

    def GetIPInfo(self, ip, timezone=False) :
        """Same as GetCity and GetCountry, but a baseurl is required.  This is for if you want to use a different server that uses the the php scripts on ipinfodb.com."""
        passdict = {"format":"json", "key":self.apikey, "ip":ip}
        if timezone :
            passdict["timezone"] = "true"
        else :
            passdict["timezone"] = "false"
        urldata = urllib.urlencode(passdict)
        url = self.baseurl + "?" + urldata
        urlobj = urllib2.urlopen(url)
        data = urlobj.read()
        urlobj.close()
        datadict = json.loads(data)
        return datadict
