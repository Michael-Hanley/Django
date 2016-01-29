from django.conf.urls import url, include
from django.contrib import admin

from .views import ingredient_view


urlpatterns = [
    url(r'^', ingredient_view),
    url(r'^admin/', include(admin.site.urls)),
]
