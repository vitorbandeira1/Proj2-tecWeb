import django_filters
from django_filters import CharFilter
from .models import Production

# class NotesFilter(django_filters.FilterSet):
#     tag = CharFilter(field_name='tag', lookup_expr='icontains')

#     class Meta:
#         model = Note
#         fields = '__all__'
#         exclude= ['title','content']
