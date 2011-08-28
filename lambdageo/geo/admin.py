from django.contrib.gis import admin
from geo.models import Building, Device, Measurement

# admin.GeoModelAdmin
admin.site.register(Building, admin.OSMGeoAdmin)
admin.site.register(Device, admin.OSMGeoAdmin)
admin.site.register(Measurement, admin.OSMGeoAdmin)
