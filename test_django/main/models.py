from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
TYPES = (
    ('python', 'Python'),
    ('django', 'Django'),
    ('backend', 'Backend'),
    ('frontend', 'Frontend'),
)


class NewsModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Title')
    img = models.ImageField(null=True, blank=True,
                            upload_to='static/images_from_user/%Y/%m/%d/')
    type = models.CharField(max_length=20, choices=TYPES,
                            default='python',
                            verbose_name='Type of news')
    text_news = models.TextField(verbose_name='Text news')
    date = models.DateTimeField(default=datetime.now(), verbose_name="Date")

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-date', 'title']
