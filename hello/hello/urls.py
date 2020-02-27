from django.conf.urls import url
from django.urls import path, re_path
from django.contrib import admin
from DjedaysAcademy import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #re_path(r'^djeday$', views.about),
    re_path(r'^candidat$', views.contact),
    re_path(r'^question$', views.question),
    re_path(r'^djedays$', views.JediListView),
    path('', views.index),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
