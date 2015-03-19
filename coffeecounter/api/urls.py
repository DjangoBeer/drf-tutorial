from .views import BadgeViewSet, ConsumptionViewSet

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'badges', BadgeViewSet)
router.register(r'consumptions', ConsumptionViewSet, base_name='consumption')

urlpatterns = [
    url(r'^', include(router.urls)),
]
