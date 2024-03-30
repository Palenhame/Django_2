from django.contrib import admin

from test_django.voting.models import VotingModel


@admin.register(VotingModel)
class VotingModelAdmin(admin.ModelAdmin):
    pass
