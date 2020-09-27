from django.contrib import admin

from .models import Blog

# admin.sites.AdminSite(Blog)
@admin.register(Blog)
class Blog(admin.ModelAdmin):
    pass
