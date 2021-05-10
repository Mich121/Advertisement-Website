import django_filters
from .models import Advertisement

class Filters(django_filters.FilterSet):
    class Meta:
        model = Advertisement
        fields = {
            'title': ['icontains'],
        }