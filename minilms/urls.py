from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('subjects/', include('subjects.urls')),
    path('admin/', admin.site.urls),
]
