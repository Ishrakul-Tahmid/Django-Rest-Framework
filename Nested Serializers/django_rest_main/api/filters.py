import django_filters
from employees.models import Employee

class EmployeeFilter(django_filters.FilterSet):
    emp_id = django_filters.CharFilter(lookup_expr='icontains')
    designation = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ['emp_id','designation']