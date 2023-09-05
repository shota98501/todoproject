from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('todoapp/', include('todoapp.urls')),
    path('admin/', admin.site.urls),
]
