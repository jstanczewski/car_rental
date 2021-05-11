from django.contrib import admin
from viewer.models import Car, CarType, CarClass, Location, Contract, Client

admin.site.register(Car)
admin.site.register(CarType)
admin.site.register(CarClass)
admin.site.register(Location)
admin.site.register(Contract)
admin.site.register(Client)
