import os

from django.core.validators import FileExtensionValidator
from django.db.models import Model, CharField, FloatField, DateField, IntegerField, ForeignKey, \
    DO_NOTHING, EmailField, ImageField


def get_upload_path(instance, filename):
    return os.path.join(f"cars/car_{instance.id}", filename)


class Car(Model):
    model = CharField(max_length=50)
    price = FloatField()
    prod_year = DateField()
    mileage = IntegerField()
    capacity = IntegerField()
    image = ImageField(
        null=True,
        blank=True,
        upload_to=get_upload_path,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    "bmp",
                    "jpg",
                    "jpeg",
                    "jpe",
                    "gif",
                    "tif",
                    "tiff",
                    "png",
                ]
            )
        ],
    )

    type_id = ForeignKey('CarType', on_delete=DO_NOTHING)
    car_class = ForeignKey('CarClass', on_delete=DO_NOTHING)
    location_id = ForeignKey('Location', on_delete=DO_NOTHING)

    def __str__(self):
        return self.model

    def __repr__(self):
        return self.location_id


class CarType(Model):
    type = CharField(max_length=20)

    def __str__(self):
        return self.type


class CarClass(Model):
    car_class = CharField(max_length=20)

    def __str__(self):
        return self.car_class


class Location(Model):
    address = CharField(max_length=100)
    capacity = IntegerField()
    city = CharField(max_length=20, default=None)

    def __str__(self):
        return self.city

    def __repr__(self):
        return self.city


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
