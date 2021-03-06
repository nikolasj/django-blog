from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from blog.serializers import UserBlogSerializer
from .permissions import IsOwnerProfile
from .forms import ImageFileUploadForm, ChangePassForm, ProfileForm, WebSiteForm
from .models import Profile
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from . import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.parsers import MultiPartParser
from rest_framework import status

User = get_user_model()


class ProfileViewSet(RetrieveModelMixin, GenericViewSet):
    permission_classes = (IsOwnerProfile,)
    parser_classes = (MultiPartParser,)

    def get_queryset(self):
        return User.objects.all().select_related('profile_set')

    def get_serializer_class(self):
        if self.action == "retrieve":
            return serializers.UserSerializer
        elif self.action == "update_image":
            return serializers.UploadImageSerializer


        return serializers.UserSerializer

    def update_image(self, request):
        print(request.FILES)
        serializer = self.get_serializer(data=request.data, instance=request.user.profile_set)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), id=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj

    def delete_image(self, request):
        user = self.get_object()
        profile = user.profile_set
        if profile.is_default_image():
            return Response({"detail": "This is default image!"}, status=status.HTTP_400_BAD_REQUEST)

        profile.set_default_image()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileViewAvatarSet(RetrieveModelMixin, GenericViewSet):
    permission_classes = (IsOwnerProfile,)
    parser_classes = (MultiPartParser,)

    def get_queryset(self):
        return User.objects.all().select_related('profile_set')

    def get_serializer_class(self):
        if self.action == "retrieve":
            return serializers.UserSerializer
        elif self.action == "update_image":
            return serializers.UploadImageAvatarSerializer

        return serializers.UserSerializer

    def update_image(self, request):
        print(request.FILES)
        serializer = self.get_serializer(data=request.data, instance=request.user.profile_set)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TemplateProfileViewSet(ProfileViewSet):
    template_name = 'account/profile.html'
    renderer_classes = (TemplateHTMLRenderer,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, template_name=self.template_name)


class UserProfileView(GenericAPIView):
    permission_classes = (IsOwnerProfile,)
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id).select_related('profile_set')

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), id=self.request.user.id)
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, )


class TemplateUserProfileView(UserProfileView):
    template_name = 'account/profile.html'
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        response = super().get(request)
        response.template_name = self.template_name
        return response
