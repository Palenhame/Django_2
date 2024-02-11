from django.contrib import admin
from django.urls import path, include
from .views import main, other, form, news
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', news, name='news'),
    path('form', form, name='form'),
    # path('news', news, name='news'),
    path('<int:page>', other, name='other'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)