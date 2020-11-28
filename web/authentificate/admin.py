from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.utils.translation import gettext_lazy as _

from blog.models import Blog

User = get_user_model()


class BlogInline(admin.StackedInline):
    model = Blog
    extra = 1
    verbose_name_plural = 'Blog'


@admin.register(User)
class CustomerAdmin(UserAdmin):
    list_per_page = 30
    list_display = ('email', 'get_full_name', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('is_active',)
    inlines = (BlogInline,)
    ordering = ()
    fieldsets = (
        (_('General'), {
            'fields': ('password',)
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'email',)
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )
