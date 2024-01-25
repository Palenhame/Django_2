from django.contrib import admin
from django.urls import path
from .views import main

app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main')
]
