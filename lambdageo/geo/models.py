from django.contrib.gis.db import models

class Building(models.Model):
    name = models.TextField()

    poly = models.PolygonField()
    objects = models.GeoManager()

    @models.permalink
    def get_absolute_url(self):
        return ('geo.views.building', [str(self.id)])

    def __unicode__(self):
        return self.name

class Device(models.Model):
    user_agent = models.TextField()

    def __unicode__(self):
        return self.user_agent

class Measurement(models.Model):
    device = models.ForeignKey(Device)
    ip = models.IPAddressField()
    datetime = models.DateTimeField()
    location = models.PointField()

    objects = models.GeoManager()

    def __unicode__(self):
        return self.location.wkt
