from django_filters import ChoiceFilter
from viewer.models import Car, Location, CarClass, CarType
import django_filters


location_choices = []
for obj in Location.objects.all():
    location_choices.append((obj.id, obj.city))
location_choices = tuple(location_choices)

car_type_choices = []
for obj in CarType.objects.all():
    car_type_choices.append((obj.id, obj.type))
car_type_choices = tuple(car_type_choices)

car_class_choices = []
for obj in CarClass.objects.all():
    car_class_choices.append((obj.id, obj.car_class))
car_class_choices = tuple(car_class_choices)


class UserFilter(django_filters.FilterSet):
    model = django_filters.CharFilter(lookup_expr="icontains", label="Model")
    price = django_filters.NumberFilter(lookup_expr="lte", label="Price")
    location_id = ChoiceFilter(choices=location_choices, label="Location")
    type_id = ChoiceFilter(choices=car_type_choices, label="Type")
    car_class = ChoiceFilter(choices=car_class_choices, label="Class")
    prod_year = django_filters.NumberFilter(
        lookup_expr="year__gte", label="Not older than"
    )
    capacity = django_filters.NumberFilter(lookup_expr="gte", label="Minimum capacity")

    class Meta:
        model = Car
        fields = [
            "model",
            "price",
            "location_id",
            "prod_year",
            "capacity",
            "type_id",
            "car_class",
        ]
