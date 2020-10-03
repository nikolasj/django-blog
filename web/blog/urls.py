from django.urls import path
from .views import IndexView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail')
]
