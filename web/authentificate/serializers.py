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


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for user profile objects."""

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def cleaned_data(self, user):
        serializer = UserProfileSerializer(instance=user)
        return serializer.data

    def create(self, validated_data):
        """Create and return a new user."""
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
