from django.urls import path
from .views import IndexView

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:id>', D.as_view(), name='detail')
]
