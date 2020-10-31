from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView
from rest_framework.views import APIView
from .forms import CommentForm

from .models import Blog, Comment


class IndexView(ListView):
    template_name = 'blog/post_list.html'
    queryset = Blog.published.order_by('publish')
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    slug_field = 'slug'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['comments'] = Comment.objects.filter(blog=self.get_object())
        data['form'] = CommentForm()
        return data

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return Blog.published.get(slug=slug)

    def get_queryset(self):
        return Blog.published.all()


class CommentAddView(View):
    def post(self, request, slug, *args, **kwargs):
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.blog = Blog.published.get(slug=slug)
            form.save()
        print(request.POST)
        return redirect(reverse('blog:detail', kwargs={'slug': slug}))
