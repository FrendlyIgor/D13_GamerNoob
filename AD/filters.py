from django_filters import FilterSet 
from .models import AD
 
 
# создаём фильтр
class ADFilter(FilterSet):
    
    class Meta:
        model = AD

        fields = {
            'author' : ['exact'],
            'title' : ['icontains'],
            'dataCategory': ['gt'] 
        }