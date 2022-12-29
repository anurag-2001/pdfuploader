from django.urls import path
from api import views

urlpatterns = [
  path('pdf/', views.ProfileView.as_view(), name='resume'),
  path('list/', views.ProfileView.as_view(), name='list')
]