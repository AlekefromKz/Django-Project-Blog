from django.contrib import admin
from .models import Post, Comment

# admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'text', 'published_date')
    list_display_links = ('title', 'text')
    search_fields = ('title', 'text', 'author__username')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
