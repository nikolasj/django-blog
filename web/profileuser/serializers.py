from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile
from blog.serializers import UserBlogSerializer

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('phone_number', 'website', 'image', 'gender', 'signature')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(source='profile_set')
    phone_number = serializers.CharField(source='profile_set.phone_number')
    posts = UserBlogSerializer(source='blog_posts', many=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_active', 'phone_number', 'posts', 'profile')
