from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name = 'Test'

