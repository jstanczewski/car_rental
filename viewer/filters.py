from viewer.models import Car
import django_filters


class UserFilter(django_filters.FilterSet):
    model = django_filters.CharFilter(lookup_expr='icontains', label='Model')
    price = django_filters.NumberFilter(label='Price')

    class Meta:
        model = Car
        fields = ['model', 'price', 'location_id', 'prod_year', 'mileage', 'capacity', 'type_id', 'car_class']

