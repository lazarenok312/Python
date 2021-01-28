from django.contrib import admin

from .models import Post, Comment


# Register your models here.
class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'user', 'body']}),
        ('Date info', {'fields': ['pub_date']}),
        ]
    inlines = [CommentInLine]

    list_display = ('title', 'pub_date')
    list_filter = ['pub_date', 'user']
    search_fields = ['body', 'title']


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post', {'fields': ['post']}),
        (None, {'fields': ['user', 'body']}),
        ('Date info', {'fields': ['pub_date']}),
        ]
        
    list_display = ('post', 'user', 'pub_date', 'body')
    list_filter = ['pub_date', 'user', 'post']
    search_fields = ['body']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
