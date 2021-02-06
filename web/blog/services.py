from .models import Blog, Comment


class BlogService:
    @staticmethod
    def get_blogs():
        return Blog.objects.all()

    @staticmethod
    def get_blog_by_slug(slug):
        return Blog.objects.get(slug=slug)

    @staticmethod
    def get_comments():
        return Comment.objects.all()
