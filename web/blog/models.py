from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.text import slugify
from .managers import PublishedManager
User = get_user_model()


def poster_upload_to(instance, file):
    now = timezone.now()
    return f"blog_images/{instance.author}/{file}"


class Blog(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200)
    slug = models.SlugField(verbose_name='Url', allow_unicode=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField('Content')
    poster = models.ImageField('Poster', upload_to=poster_upload_to, default='blog_images/no_image.png')
    publish = models.DateTimeField('Publish date', auto_now_add=True)
    draft = models.BooleanField('Draft', default=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.title}: {self.author.email}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True).lower()
        return super().save(*args, **kwargs)

    def get_comments(self):
        # print(dir(self))
        return self.blog_comment.filter(parent__isnull=True).order_by('-created_date')

    def get_absolute_url(self):
        return reverse_lazy('blog:detail', kwargs={'slug': self.slug})

    def is_published(self):
        return not self.draft

    is_published.short_description = 'Published'
    is_published.boolean = True


class Comment(models.Model):
    # author = models.CharField('Author', max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_set')
    comment = models.TextField('Comment')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parent_comment', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.author}: {self.comment[:10]}"
