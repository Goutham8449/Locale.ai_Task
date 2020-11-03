from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (IsAuthenticatedOrReadOnly, IsAuthenticated)
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from .models import CustomUser, Trip
from .serializers import UserSerializer, TripSerializer
# Create your views here.


class TripViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    """
    def get_queryset(self, *args, **kwargs):
        # return Users.objects.all()
        print(self.request.user)
        return User.objects.filter(username=self.request.user)
    """
