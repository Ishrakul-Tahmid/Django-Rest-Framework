import django_filters
from .models import Project


class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    tech_stack = django_filters.CharFilter(field_name='tech_stack', lookup_expr='icontains')


    class Meta:
        model = Project
        fields = ['name', 'tech_stack', 'created_at']