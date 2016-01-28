from django.conf.urls import url
from .views import ingredient_view


urlpatterns = [
    url(r'^', ingredient_view),
]
