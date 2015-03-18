from .models import Badge, Consumption
from .serializers import BadgeSerializer, ConsumptionSerializer
from .permissions import IsSuperUserOrReadOnly
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class BadgeList(APIView):
    """
    List all badges or create a new badge.
    """
    permission_classes = (IsSuperUserOrReadOnly,)

    def get(self, request, format=None):
        badges = Badge.objects.all()
        serializer = BadgeSerializer(badges, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BadgeSerializer(data=request.data)
        self.check_object_permissions(request, serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BadgeDetail(APIView):
    """
    Retrieve, update or delete a badge instance.

    If you're writing your own views and want to enforce object level permissions,
    or if you override the get_object method on a generic view, then you'll need to
    explicitly call the .check_object_permissions(request, obj) method on the view
    at the point at which you've retrieved the object.
    """
    permission_classes = (IsSuperUserOrReadOnly,)

    def get_object(self, pk):
        try:
            return Badge.objects.get(pk=pk)
        except Badge.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        badge = self.get_object(pk)
        self.check_object_permissions(request, badge)
        serializer = BadgeSerializer(badge)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        badge = self.get_object(pk)
        self.check_object_permissions(request, badge)
        serializer = BadgeSerializer(badge, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        badge = self.get_object(pk)
        self.check_object_permissions(request, badge)
        serializer = BadgeSerializer(badge, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        badge = self.get_object(pk)
        self.check_object_permissions(request, badge)
        badge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ConsumptionList(APIView):
    """
    List all consumptions.
    """
    def get(self, request, format=None):
        consumptions = Consumption.objects.all()
        serializer = ConsumptionSerializer(consumptions, many=True)
        return Response(serializer.data)


class ConsumptionListPerUser(APIView):
    """
    List all the auth users consumptions or create a new consumption.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        consumptions = Consumption.objects.filter(user=self.request.user)
        serializer = ConsumptionSerializer(consumptions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data['user'] = self.request.user.pk
        serializer = ConsumptionSerializer(data=request.data)
        self.check_object_permissions(request, serializer)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
