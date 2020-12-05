from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import IndexView, BlogDetailView, CommentAddView, BlogAPIView, CommentAPIAddView

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<str:slug>/', BlogDetailView.as_view(), name='detail'),
    path('api/blog/', BlogAPIView.as_view(), name='blog_api'),
    path('api/comment/', CommentAPIAddView.as_view(), name='comment_api'),
    path('<str:slug>/add-comment/', login_required(CommentAddView.as_view()), name='add_comment'),
]
