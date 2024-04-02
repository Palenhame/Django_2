from django.contrib import admin
import psycopg2
from .models import VotingModel


@admin.register(VotingModel)
class VotingModelAdmin(admin.ModelAdmin):
    pass 
