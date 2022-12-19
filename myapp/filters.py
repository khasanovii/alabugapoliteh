import django_filters
from .models import People

class PeopleFilter(django_filters.FilterSet):
    age = django_filters.AllValuesFilter()

    class Meta:
        model = People
        fields = ['age']