from django.contrib import admin

from .models import BlogModel

# admin.sites.AdminSite(Blog)
@admin.register(BlogModel)
class Blog(admin.ModelAdmin):
    pass
