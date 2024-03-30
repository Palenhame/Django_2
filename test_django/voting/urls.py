from django.urls import path

from voting import views

app_name = 'voting'
urlpatterns = [
    path('voting/', views.voting, name='voting')
]
