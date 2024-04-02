from django.urls import path

from . import views

app_name = 'voting'
urlpatterns = [
    path('<int:voting_id>', views.voting, name='voting')
]
