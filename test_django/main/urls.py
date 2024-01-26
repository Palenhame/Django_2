from django.contrib import admin
from django.urls import path
from .views import main, other, form

app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('form', form, name='form'),
    path('<int:page>', other, name='other'),
]
