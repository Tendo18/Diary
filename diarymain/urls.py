
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('diary/', admin.site.urls),
    path('api/', include('diaryapi.urls')),
]
