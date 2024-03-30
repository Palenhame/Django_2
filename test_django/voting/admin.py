from django.contrib import admin

from Django_2.test_django.voting.models import VotingModel


# Register your models here.
@admin.register(VotingModel)
class VotingModelAdmin(admin.ModelAdmin):
    pass
