from django.urls import path
from .views import IndexView, BlogDetailView, CommentAddView

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<str:slug>/', BlogDetailView.as_view(), name='detail'),
    path('<str:slug>/add-comment/', CommentAddView.as_view(), name='add_comment')
]
