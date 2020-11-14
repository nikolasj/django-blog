from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog, Comment


@admin.register(Blog)
class Blog(SummernoteModelAdmin):
    list_display = ('id', 'title', 'author', 'draft', 'slug')
    list_display_links = ('title',)
    # prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'author', 'content', 'draft', 'poster',)
    summernote_fields = ('content',)
    # readonly_fields = ('author',)
    # actions_on_top = True
    # actions_on_bottom = True
    # actions_selection_counter = False


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
