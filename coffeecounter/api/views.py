from .models import Badge, Consumption
from .serializers import BadgeSerializer, ConsumptionSerializer
from .permissions import IsSuperUserOrReadOnly
from rest_framework import permissions
from rest_framework import generics


class BadgeList(generics.ListCreateAPIView):
    """
    List all badges or create a new badge.
    """
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class BadgeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a badge instance.
    """
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class ConsumptionList(generics.ListAPIView):
    """
    List all consumptions.
    """
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer


class ConsumptionListPerUser(generics.ListCreateAPIView):
    """
    List all the auth users consumptions or create a new consumption.
    """
    serializer_class = ConsumptionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Consumption.objects.filter(user=self.request.user)
