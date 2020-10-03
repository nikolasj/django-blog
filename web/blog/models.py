from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from .managers import PublishedManager


def poster_upload_to(instance, file):
    now = timezone.now()
    return f"blog_images/{instance.author}/{file}"


class Blog(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200)
    slug = models.SlugField(verbose_name='Url', allow_unicode=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField('Content')
    poster = models.ImageField('Poster', upload_to=poster_upload_to, default='blog_images/no_image.png')
    publish = models.DateTimeField('Publish date', auto_now_add=True)
    draft = models.BooleanField('Draft', default=True)

    published = PublishedManager()

    objects = models.Manager()

    def __str__(self):
        return f"{self.title}: {self.author.username}"
