from django.urls import path
from .views import register, LoginUser, user_logout, account


app_name = 'user'
urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('test/', account, name='test'),


]
