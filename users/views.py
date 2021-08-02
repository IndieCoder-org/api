from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated

from .serializers import UserSerializer, UserUpdateSerializer


@api_view(['GET'])
def user_details(request):
    """
    Returns details on the currently logged in user
    """
    if request.user.is_authenticated:
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    else:
        raise NotAuthenticated()


@api_view(['POST'])
def user_create(request):
    """
    Creates a new user
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def user_update(request, pk):
    """
    Updates a new user
    """
    user = get_user_model().objects.get(id=pk)
    serializer = UserUpdateSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
