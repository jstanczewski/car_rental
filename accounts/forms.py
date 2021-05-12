from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import CharField, IntegerField, EmailField


class SignUpForm(UserCreationForm):
    first_name = CharField(max_length=50)
    second_name = CharField(max_length=50)
    document_number = CharField(max_length=15)
    age = IntegerField()
    address = CharField(max_length=100)
    email_address = EmailField()
    phone_number = CharField(max_length=15)

    class Meta:
        model = Profile
        fields = (
            "first_name",
            "second_name",
            "document_number",
            "age",
            "address",
            "email_address",
            "phone_number",
            "password1",
            "password2",
        )
