from django.urls import path
from .views import register


app_name = 'user'
urlpatterns = [
    path('login/', None, name='login'),
    path('logout/', None, name='logout'),
    path('register/', register, name='register'),
]
