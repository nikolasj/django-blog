from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
from .serializers import *
from rest_framework.response import Response
from .models import Blog, Comment
from authentificate.models import User

class BlogAPIView(GenericAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.all()

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class CommentAPIAddView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Comment.objects.all()

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        print(self.request.user)
        blog = Blog.objects.get(slug='blog-1')

        serializer.save(author=self.request.user, blog=blog)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(status=status.HTTP_200_OK)

    # def perform_create(self, serializer):
    #     print(User)
    #     author = get_object_or_404(User, id=self.request.data.get('id'))
    #     return serializer.save(author=author)

    # def post(self, request, *args, **kwargs):
    #     print(request.POST)
    #
    #
    #     return Response(status=status.HTTP_200_OK)


class IndexView(ListView):
    template_name = 'blog/post_list.html'
    queryset = Blog.objects.order_by('publish')
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    slug_field = 'slug'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['comments'] = Comment.objects.filter(blog=self.get_object())
        if self.request.user.is_authenticated:
            data['form'] = CommentForm()
        return data

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return Blog.objects.get(slug=slug)

    def get_queryset(self):
        return Blog.objects.all()


class CommentAddView(APIView):

    def post(self, request, slug, *args, **kwargs):
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.blog = Blog.objects.get(slug=slug)
            user = request.POST.get('author')
            form.author_id = int(user)
            if request.POST.get('parent'):
                form.parent_id = int(request.POST.get('parent'))
                # form.parent = Comment.objects.get(id=int(request.POST.get('parent')))
            # print(request.POST)
            form.save()
        return redirect(reverse('blog:detail', kwargs={'slug': slug}))
