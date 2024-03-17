from django.contrib import admin
from django.urls import path, include
from .views import main, other, form, news, voting,error
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('404', error),
    path('', news, name='news'),
    path('form', form, name='form'),
    # path('news', news, name='news'),
    path('<int:page>', other, name='other'),
    path('voting', voting, name='voting')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)