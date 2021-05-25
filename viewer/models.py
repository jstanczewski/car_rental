import os
from django.db import models
from accounts.models import Profile
from django.core.validators import FileExtensionValidator
from django.db.models import (
    Model,
    CharField,
    FloatField,
    DateField,
    IntegerField,
    ForeignKey,
    EmailField,
    ImageField,
)


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

    type_id = ForeignKey("CarType", on_delete=models.CASCADE)
    car_class = ForeignKey("CarClass", on_delete=models.CASCADE)
    location_id = ForeignKey("Location", on_delete=models.CASCADE)

    def __str__(self):
        return self.model

    def __repr__(self):
        return self.model

    def save(self, *args, **kwargs):
        location_capacity = self.location_id.capacity
        for _ in Car.objects.filter(location_id=self.location_id):
            location_capacity -= 1
        if location_capacity <= 0:
            raise IndexError(f'{self.location_id} capacity overloaded')
        else:
            super().save(*args, **kwargs)


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

    car_id = ForeignKey(Car, on_delete=models.CASCADE)
    profile_id = ForeignKey(Profile, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.profile_id}, {self.car_id}, ({self.date_from} - {self.date_to})"


class Client(Model):
    first_name = CharField(max_length=50)
    second_name = CharField(max_length=50)
    document_number = CharField(max_length=15)
    age = IntegerField()
    address = CharField(max_length=100)
    email_address = EmailField()
    phone_number = CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.second_name}, {self.email_address}"
