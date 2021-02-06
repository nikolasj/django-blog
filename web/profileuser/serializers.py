from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile
from blog.serializers import UserBlogSerializer
from django.conf import settings

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('phone_number', 'website', 'image', 'gender', 'signature')


class UploadImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    def validate(self, attrs):
        print("validate", attrs)
        return attrs

    def validate_image(self, image):
        print("validate_image", image)
        print(dir(image))
        if image.size > settings.AVATAR_IMAGE_MAX_SIZE * 1024 * 1024:
            raise serializers.ValidationError(f"Max size is {settings.AVATAR_IMAGE_MAX_SIZE}")
        return image

    class Meta:
        model = Profile
        fields = ('image',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(source='profile_set')
    phone_number = serializers.CharField(source='profile_set.phone_number')
    posts = UserBlogSerializer(source='blog_posts', many=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_active', 'phone_number', 'posts', 'profile')
