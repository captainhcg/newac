from django.db import models
from datetime import datetime, timedelta
import settings

# Create your models here.
class Visitor(models.Model):
    ip_address 	= models.IPAddressField(default='0.0.0.0', db_index=True)
    visit_date 	= models.DateField(db_index=True)
    ip_map      = models.ForeignKey('IPMap', blank=True, null=True, on_delete=models.SET_NULL, db_index=True)
    created_at 	= models.DateTimeField(auto_now_add=True)
    updated_at 	= models.DateTimeField(auto_now=True)

    @staticmethod
    def findDuplicate(visitor):
        hour_ago = datetime.now() + timedelta(hours = 1)
        target = Visitor.objects.filter(ip_address = visitor.ip_address, created_at__gte = hour_ago)
        if target:
            return target
        else:
            return False

    def __unicode__(self):
        return ""


class IPMap(models.Model):
    ip_address      = models.IPAddressField(unique=True, db_index=True, default='0.0.0.0')
    country_code    = models.CharField(max_length=4, db_index=True, blank=True, null=True)
    country_name    = models.CharField(max_length=32, blank=True, null=True)
    city_name       = models.CharField(max_length=64, db_index=True, blank=True, null=True)
    latitude        = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    longtitude      = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    latitude_int    = models.IntegerField(db_index=True, blank=True, null=True)
    longtitude_int  = models.IntegerField(db_index=True, blank=True, null=True)
    region_name     = models.CharField(max_length=64, db_index=True, blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "IP %s is in %s, %s, %s" % (self.ip_address, self.city_name, self.region_name, self.country_name)

    def createMapFromInfo(self, info):
        self.ip_address = info['ipAddress']
        self.country_code = info['countryCode']
        self.country_name = info['countryName']
        self.city_name = info['cityName']
        self.latitude = info['latitude']
        self.longtitude = info['longitude'] 
        self.region_name = info['regionName']

    def save(self, *args, **kwargs):
        try:
            self.latitude_int   = int(round(float(self.latitude), 0))
            self.longtitude_int = int(round(float(self.longtitude), 0))
        except:
            if settings.DEBUG == True:
                print "ERROR: cannot convert latitude and longtitude to int for ip %s" % self.ip_address

        super(IPMap, self).save(*args, **kwargs)
