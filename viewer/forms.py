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
        if result["insurance_1_id"] is not None and (result["insurance_1_id"] == result["insurance_2_id"] or result["insurance_1_id"] == result["insurance_3_id"] or result["insurance_1_id"] == result["insurance_4_id"]):
            raise ValidationError("Cannot choose same insurance more than once!")
        if result["insurance_2_id"] is not None and (result["insurance_2_id"] == result["insurance_3_id"] or result["insurance_2_id"] == result["insurance_4_id"]):
            raise ValidationError("Cannot choose same insurance more than once!")
        if result["insurance_3_id"] is not None and (result["insurance_3_id"] == result["insurance_4_id"]):
            raise ValidationError("Cannot choose same insurance more than once!")
        return result
