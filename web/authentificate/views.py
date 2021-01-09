from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from .serializers import UserProfileSerializer
from rest_framework.response import Response
# from .models import User
User = get_user_model()

class UserProfileViewSet(GenericViewSet):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.all()

    def get(self, request, slug=None):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(serializer.cleaned_data(user), status=status.HTTP_201_CREATED)