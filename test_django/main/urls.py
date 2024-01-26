from django.contrib import admin
from django.urls import path
from .views import main, other

app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('<int:page>', other, name='other')
]
