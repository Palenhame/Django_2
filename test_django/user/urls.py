from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import register, LoginUser


app_name = 'user'
urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
