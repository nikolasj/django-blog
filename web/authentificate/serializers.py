from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # full_name = serializers.CharField(source='get_full_name')
    get_full_name = serializers.CharField(min_length=5)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id', 'email', 'get_full_name')
