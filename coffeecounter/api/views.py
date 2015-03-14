from .models import Badge
from .serializers import BadgeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BadgeList(APIView):
    """
    List all badges or create a new badge.
    """
    def get(self, request, format=None):
        badges = Badge.objects.all()
        serializer = BadgeSerializer(badges, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BadgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BadgeDetail(APIView):
    """
    Retrieve, update or delete a badge instance.
    """
    def get_object(self, pk):
        try:
            return Badge.objects.get(pk=pk)
        except Badge.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        badge = self.get_object(pk)
        serializer = BadgeSerializer(badge)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        badge = self.get_object(pk)
        serializer = BadgeSerializer(badge, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        badge = self.get_object(pk)
        serializer = BadgeSerializer(badge, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        badge = self.get_object(pk)
        badge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
