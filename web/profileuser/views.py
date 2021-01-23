from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.response import Response
from .permissions import IsOwnerProfile
from .forms import ImageFileUploadForm, ChangePassForm, ProfileForm, WebSiteForm
from .models import Profile
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from rest_framework.renderers import TemplateHTMLRenderer

User = get_user_model()


class ProfileViewSet(ModelViewSet):
    serializer_class = UserSerializer
    template_name = 'account/profile.html'
    renderer_classes = (TemplateHTMLRenderer,)
    permission_classes = (IsOwnerProfile,)

    def get_queryset(self):
        return User.objects.all().select_related('profile_set')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, template_name=self.template_name)

# def user_site(request, user):
#     if request.method == 'POST':
#         user = request.POST.get("user")
#         web_url = request.POST.get("web_url")
#         profile = get_object_or_404(Profile, user=request.user)
#         print(user, web_url)
#         profile.website = web_url
#         profile.save()
#         return JsonResponse({'error': False, 'message': 'Uploaded Successfully', 'website': web_url})
#
#
# def image_upload_ajax(request, user):
#     profile = request.user.profile
#     if request.method == 'POST':
#         form = ImageFileUploadForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
#         else:
#             return JsonResponse({'error': True, 'errors': form.errors})
#
#
# class ProfileView(View):
#     template_name = 'account/profile/main_profile_page.html'
#     context_object_name = 'profile'
#
#     def get(self, request, id=None, *args, **kwargs):
#         profile = get_object_or_404(User, id=id)
#         print(profile)
#         upload_image_form = ImageFileUploadForm()
#         change_password = ChangePassForm()
#         profile_form = ProfileForm(instance=profile)
#         # print(dir(profile_form.data.dict()))
#
#         web_site_form = WebSiteForm()
#         return render(request, 'account/profile.html', {'user_profile': profile,
#                                                         'upload_image_form': upload_image_form,
#                                                         'change_password': change_password,
#                                                         'profile_form': profile_form,
#                                                         'web_site_form': web_site_form,
#                                                         })
#
#     def post(self, request, id=None, *args, **kwargs):
#         obj = get_object_or_404(User, id=id)
#         #
#         form = ProfileForm(request.POST or None, instance=obj)
#         context = {'form': form}
#         if form.is_valid():
#             print('form validate')
#             form = form.save(commit=False)
#             form.save()
#             messages.success(request, "You successfully updated the user")
#             print(form)
#             context = {'profile_form': form}
#
#             return render(request, 'account/profile.html', context)
#         else:
#             context = {'profile_form': obj,
#                        'error': 'The form was not updated successfully.'}
#         print('render')
#         return render(request, 'account/profile.html', context)
#
#
# @login_required
# def user_profile(request, user):
#     profile = get_object_or_404(Profile, user=user)
#     return render(request, 'app/profile.html', {'profile': profile})
