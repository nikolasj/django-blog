from rest_framework import serializers
from .models import Blog, Comment, User
from authentificate.serializers import UserSerializer


class ShortUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('get_full_name',)


class ShortBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('author', 'publish',)


class BlogSerializer(serializers.ModelSerializer):
    author = ShortUserSerializer(read_only=True)

    class Meta:
        model = Blog
        exclude = ('content',)


class CommentSerializer_(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    blog = ShortBlogSerializer(read_only=True)
    parents = serializers.SerializerMethodField(method_name='get_parents')

    def get_parents(self, obj):
        data = []
        for parent in obj.parent_comment.all():
            parent_data = {
                "id": parent.id,
                "author": parent.author.email,
                "comment": parent.comment
            }
            data.append(parent_data)
        return data

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'parent')

    def cleaned_data(self, comment):
        serializer = CommentSerializer_(instance=comment)
        return serializer.data

    def create(self, validated_data):
        request = self.context.get('request')
        blog = self.context.get('blog')
        comment = Comment(**validated_data)
        comment.author = request.user
        comment.blog = blog
        comment.save()
        self.cleaned_data(comment)

        return comment
