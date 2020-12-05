from rest_framework import serializers
from .models import Blog, Comment


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    blog = serializers.StringRelatedField(many=False)

    class Meta:
        model = Comment
        fields = '__all__'
