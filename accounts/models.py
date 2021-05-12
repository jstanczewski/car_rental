import django.db.models as models
from django.contrib.auth.models import User
from django.db.models import Model, CharField, IntegerField, EmailField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = CharField(max_length=50)
    second_name = CharField(max_length=50)
    document_number = CharField(max_length=15)
    age = IntegerField()
    address = CharField(max_length=100)
    email_address = EmailField()
    phone_number = CharField(max_length=15)

    def __str__(self):
        return f'{self.first_name}, {self.second_name}, {self.email_address}'

    def __repr__(self):
        return f'{self.first_name}, {self.second_name}, {self.email_address}'
