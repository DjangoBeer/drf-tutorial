from .models import Badge, Consumption
from .serializers import BadgeSerializer, ConsumptionSerializer
from .permissions import IsSuperUserOrReadOnly
from rest_framework import permissions
from rest_framework import mixins
from rest_framework import generics


class BadgeList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    """
    List all badges or create a new badge.
    """
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = (IsSuperUserOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BadgeDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    """
    Retrieve, update or delete a badge instance.

    If you're writing your own views and want to enforce object level permissions,
    or if you override the get_object method on a generic view, then you'll need to
    explicitly call the .check_object_permissions(request, obj) method on the view
    at the point at which you've retrieved the object.
    """
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = (IsSuperUserOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ConsumptionList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    """
    List all consumptions.
    """
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ConsumptionListPerUser(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             generics.GenericAPIView):
    """
    List all the auth users consumptions or create a new consumption.
    """
    serializer_class = ConsumptionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Consumption.objects.filter(user=self.request.user)
