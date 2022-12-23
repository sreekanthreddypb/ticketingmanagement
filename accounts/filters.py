from dataclasses import fields
from django.forms import CharField
import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class TicketFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr="gte")
    last_date = DateFilter(field_name="date_created", lookup_expr="lte")
    title = CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['description', 'date_created']
