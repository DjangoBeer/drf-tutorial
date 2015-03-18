from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BadgeDetail, BadgeList, ConsumptionList, ConsumptionListPerUser

urlpatterns = [
    url(r'^badges/$', BadgeList.as_view()),
    url(r'^badges/(?P<pk>[0-9]+)$', BadgeDetail.as_view()),
    url(r'^consumptions/all/$', ConsumptionList.as_view()),
    url(r'^consumptions/$', ConsumptionListPerUser.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)