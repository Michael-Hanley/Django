from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from page import views

urlpatterns = patterns('',
    url(r'^api/$', views.post_list.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.post_detail.as_view()),
    )

urlpatterns = format_suffic_patterns(urlpatterns)
