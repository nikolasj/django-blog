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
    # slug_field =

    # queryset = Blog.objects.all()
    context_object_name = 'blog'
    # model = Blog

    # def get_object(self, queryset=None):
    #     id = self.kwargs.get('pk')
    #     # print(self.kwargs)
    #     return Blog.published.get(id=id)

    def get_queryset(self):
        return Blog.published.all()

# def get(self, request, id):
#     blog = Blog.published.get(id=id)
#     content = {'blog': blog}
#
#     return render(request, 'blog/post_detail.html', content)

# def get(self, request):
#     site = 'Blog site'
#     blogs = Blog.published.order_by('publish')
#     content = {'blogs': blogs, 'site': site}
#
#     return render(request, 'blog/post_list.html', content)
