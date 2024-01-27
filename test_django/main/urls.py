from django.contrib import admin
from django.urls import path
from .views import main, other, form, news

app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('form', form, name='form'),
    path('news', news, name='news'),
    path('<int:page>', other, name='other'),
]
