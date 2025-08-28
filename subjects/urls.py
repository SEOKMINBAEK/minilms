from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:id>/', views.detail, name='detail'),
  path('<int:id>/apply/', views.apply, name='apply'),
]