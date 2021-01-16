from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import ProfileView, image_upload_ajax, user_site

app_name = 'profile'

urlpatterns = [
    path('account/profile/<user>/image/', image_upload_ajax, name='image_upload'),
    path('account/profile/<int:id>/user_site/', user_site, name='user_site'),
    path('account/profile/<int:id>/', ProfileView.as_view(), name='user_profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
