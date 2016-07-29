from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('apps.blog.urls', namespace="blog")),
    url(r'^usuarios/', include('apps.usuarios.urls', namespace="usuarios")),
    ]