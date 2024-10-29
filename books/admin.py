from django.contrib import admin
from .models import About, PostImage, Comment, Terms_condition, Privacy_policy, Contact, Posts

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1
    raw_id_fields = ('post',)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    raw_id_fields = ('post',)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author_name', 'date', 'created', 'updated')
#     list_filter = ('author_name', 'date')
#     search_fields = ('title', 'body', 'author_name__username')
#     prepopulated_fields = {'slug': ('title',)}
#     inlines = [PostImageInline, CommentInline]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'uploaded_at')
    list_filter = ('post',)
    search_fields = ('post__title',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'active', 'created')
    list_filter = ('active', 'created', 'post')
    search_fields = ('name', 'email', 'body')

@admin.register(Privacy_policy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')

@admin.register(Terms_condition)
class TermsConditionAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'date', 'description1')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PostImageInline, CommentInline]

