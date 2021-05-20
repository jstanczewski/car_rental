from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateField, IntegerField
from datetime import date
from viewer.models import Contract


class PastDateField(DateField):
    def validate(self, value):
        super().validate(value)
        if value < date.today():
            raise ValidationError("Past dates are not allowed!")

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=result.day)


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'

    date_from = PastDateField()

    def clean(self):
        result = super().clean()
        if result["date_to"] <= date.today():
            raise ValidationError("Date to cannot come before date from")
        return result
