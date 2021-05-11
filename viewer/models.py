from django.db import models
from django.db.models import Model, CharField, FloatField, DateField, IntegerField, ForeignKey, \
    DO_NOTHING, EmailField


class Car(Model):
    model = CharField(max_length=50)
    price = FloatField()
    prod_year = DateField()
    mileage = IntegerField()
    capacity = IntegerField()

    type_id = ForeignKey('CarType', on_delete=DO_NOTHING)
    car_class = ForeignKey('CarClass', on_delete=DO_NOTHING)
    location_id = ForeignKey('Location', on_delete=DO_NOTHING)


class CarType(Model):
    type = CharField(max_length=20)


class CarClass(Model):
    car_class = CharField(max_length=20)


class Location(Model):
    address = CharField(max_length=100)
    capacity = IntegerField()


class Contract(Model):
    date_from = DateField()
    date_to = DateField()

    car_id = ForeignKey(Car, on_delete=DO_NOTHING)
    client_id = ForeignKey('Client', on_delete=DO_NOTHING)


class Client(Model):
    first_name = CharField(max_length=50)
    second_name = CharField(max_length=50)
    document_number = CharField(max_length=15)
    age = IntegerField()
    address = CharField(max_length=100)
    email_address = EmailField()
    phone_number = CharField(max_length=15)