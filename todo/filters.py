from django_filters import FilterSet
from .models import Todo

class TodoFilter(FilterSet):
    class Meta:
        model = Todo
        fields = {
            'title': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'due_date': ['exact', 'lt', 'gt'],
            'completed': ['exact'],
        }