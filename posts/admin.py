from django.contrib import admin
from .models import Post, Comment
# Register your models here.

class CommentAdminInline(admin.TabularInline):
    model = Comment
    fields = ['text']
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id' ,'title', 'is_enabled', 'created_date', 'publish_date']
    inlines = [CommentAdminInline, ]
    

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['post', 'text']
    

# admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)
