from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('apps.blog.urls', namespace=blog)),
    url(r'^$', include('apps.usuarios.urls', namespace=usuarios)),
    ]