from django.urls import path
from . import views
from AD.views import ADListView, ADDetailView

app_name = "AD"
urlpatterns = [
    path('', ADListView.as_view(), name='posts'),
    path('one_post/<int:pk>', ADDetailView.as_view(), name = 'one'),
 
]