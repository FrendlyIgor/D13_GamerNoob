from django.urls import path
from . import views
from AD.views import ADListView, ADDetailView, ADCreateView, ADUpdateView, AddLike, AddDislike

app_name = "AD"
urlpatterns = [
    path('', ADListView.as_view(), name='posts'),
    path('one_post/<int:pk>', ADDetailView.as_view(), name = 'one'),
    path('AD_add/', ADCreateView.as_view(), name='AD_add'),
    path('AD_edit/<int:pk>', ADUpdateView.as_view(), name='AD_edit'),
    path('<int:pk>/like/', AddLike.as_view(), name='like'),
    path('<int:pk>/dislike/', AddDislike.as_view(), name='dislike')
    
]