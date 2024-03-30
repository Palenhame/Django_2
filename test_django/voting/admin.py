from django.contrib import admin

from voting.models import VotingModel


@admin.register(VotingModel)
class VotingModelAdmin(admin.ModelAdmin):
    pass