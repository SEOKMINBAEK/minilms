from django.urls import path
from . import views

app_name = 'subjects'

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:id>/', views.detail, name='detail'),
  path('apply/<int:id>/', views.apply, name='apply'),
]