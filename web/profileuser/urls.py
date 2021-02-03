from django.urls import path
from django.contrib.auth.views import LogoutView
# from .views import ProfileView, image_upload_ajax, user_site
from rest_framework import routers
from .views import ProfileViewSet, TemplateProfileViewSet, UserProfileView, TemplateUserProfileView

app_name = 'profile'

router = routers.DefaultRouter()
router.register('api/profile', ProfileViewSet, basename='api_profile')
router.register('profile', TemplateProfileViewSet, basename='profile')

urlpatterns = [
    path('api/profile/', UserProfileView.as_view(), name='profile_api'),
    path('profile/', TemplateUserProfileView.as_view(), name='profile_view'),
    # path('account/profile/<user>/image/', image_upload_ajax, name='image_upload'),
    # path('account/profile/<int:id>/user_site/', user_site, name='user_site'),
    # path('account/profile/<int:id>/', ProfileView.as_view(), name='user_profile'),

    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]

urlpatterns += router.urls
