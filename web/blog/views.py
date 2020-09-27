from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView

from .models import Blog


class IndexView(APIView):
    def get(self, request):
        site = 'Blog site'
        blogs = Blog.objects.all().order_by('publish')
        content = {'blogs': blogs, 'site': site}

        return render(request, 'blog/index.html', content)
