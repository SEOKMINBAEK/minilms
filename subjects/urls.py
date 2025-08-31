from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'subjects'

router = DefaultRouter()
router.register(r'api', views.SubjectViewSet)
router.register(r'history/api', views.ApplyViewSet)

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:id>/', views.detail, name='detail'),
  path('upload_image/<int:id>/', views.upload_image, name='upload_image'),
  path('apply/<int:id>/', views.apply, name='apply'),
  path('history/', views.history, name='history'),
]

urlpatterns += router.urls