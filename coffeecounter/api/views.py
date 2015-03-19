from .models import Badge, Consumption
from .serializers import BadgeSerializer, ConsumptionSerializer
from .permissions import IsSuperUserOrReadOnly
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response


class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class ConsumptionViewSet(viewsets.ModelViewSet):
    serializer_class = ConsumptionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @list_route(methods=['get'], permission_classes=[permissions.AllowAny])
    def all(self, request):
        consumptions = Consumption.objects.all()
        serializer = ConsumptionSerializer(consumptions, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Consumption.objects.filter(user=self.request.user)
