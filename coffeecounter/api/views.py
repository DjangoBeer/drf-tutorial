from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Badge
from api.serializers import BadgeSerializer


@api_view(['GET', 'POST'])
def badge_list(request):
    """
    List all badges or create a new badge.
    """
    if request.method == 'GET':
        badges = Badge.objects.all()
        serializer = BadgeSerializer(badges, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BadgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def badge_detail(request, pk):
    """
    Retrieve, update or delete a badge.
    """
    try:
        badge = Badge.objects.get(pk=pk)
    except Badge.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BadgeSerializer(badge)
        return Response(serializer.data)

    elif request.method == 'PUT' or request.method == 'PATCH':
        partial_update = False
        serializer = BadgeSerializer(
            badge, data=request.data,
            partial=(request.method == 'PATCH')
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        badge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
