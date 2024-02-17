from django.contrib import admin
from .models import NewsModel, CommentModel

# Register your models here.
admin.site.register(NewsModel)
admin.site.register(CommentModel)
