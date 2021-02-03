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
from .serializers import UserSerializer
from rest_framework.renderers import TemplateHTMLRenderer

User = get_user_model()


class ProfileViewSet(RetrieveModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsOwnerProfile,)

    def get_queryset(self):
        return User.objects.all().select_related('profile_set')


class TemplateProfileViewSet(ProfileViewSet):
    template_name = 'account/profile.html'
    renderer_classes = (TemplateHTMLRenderer,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, template_name=self.template_name)


class UserProfileView(GenericAPIView):
    permission_classes = (IsOwnerProfile,)
    serializer_class = UserSerializer

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
