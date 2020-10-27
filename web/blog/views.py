from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from rest_framework.views import APIView

from .models import Blog


class IndexView(ListView):
    template_name = 'blog/post_list.html'
    queryset = Blog.published.order_by('publish')
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    slug_field = 'slug'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        print(self.kwargs)
        return Blog.published.get(slug=slug)

    def get_queryset(self):
        return Blog.published.all()
