from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateField, IntegerField
from datetime import date
from viewer.models import Contract


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = "__all__"

    def clean(self):
        result = super().clean()
        if result["date_to"] <= result["date_from"]:
            raise ValidationError("Date to cannot come before date from!")
        elif result["date_from"] < date.today():
            raise ValidationError("Past dates are not allowed!")
        return result
