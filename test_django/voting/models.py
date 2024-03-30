from django.db import models


# Create your models here.
class VotingModel(models.Model):
    text = models.CharField(max_length=100)
    value1 = models.CharField(max_length=20)
    value2 = models.CharField(max_length=20)
    value3 = models.CharField(max_length=20)
    value4 = models.CharField(max_length=20)
    value1_votes = models.IntegerField(default=0)
    value2_votes = models.IntegerField(default=0)
    value3_votes = models.IntegerField(default=0)
    value4_votes = models.IntegerField(default=0)
