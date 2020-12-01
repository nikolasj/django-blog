from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy, reverse

from blog.models import Blog

User = get_user_model()


class BlogInline(admin.TabularInline):
    model = Blog
    extra = 0
    verbose_name_plural = 'Blog'
    readonly_fields = ('is_published',)
    fields = ('title', 'is_published', 'slug')

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False

    def get_full_path(self, obj):
        return reverse('blog:detail', kwargs={'slug': obj.slug})


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
