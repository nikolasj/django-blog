from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token


urlpatterns = [
    path('', include('app.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('token/verify/', verify_jwt_token, name="verify_auth_token"),
    path('token/refresh/', refresh_jwt_token, name="refresh_auth_token"),
]

# handler404 = 'app.views.custom_handler404'
# handler500 = 'app.views.custom_handler500'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
