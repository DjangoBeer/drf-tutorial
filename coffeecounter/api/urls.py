from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import badge_list, badge_detail

urlpatterns = [
    url(r'^badges/$', badge_list),
    url(r'^badges/(?P<pk>[0-9]+)$', badge_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)