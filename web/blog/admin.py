from django.contrib import admin

from .models import Blog, Comment


@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'draft', 'slug')
    list_display_links = ('title',)
    # prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'author', 'content', 'draft', 'poster',)
    # readonly_fields = ('author',)
    # actions_on_top = True
    # actions_on_bottom = True
    # actions_selection_counter = False


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
