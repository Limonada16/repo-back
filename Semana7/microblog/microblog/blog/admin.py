from blog.models import HashTag, Post
from django.contrib import admin

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass

class HashTagAdmin(admin.ModelAdmin):
    pass

admin.site.register(HashTag, HashTagAdmin)
admin.site.register(Post, PostAdmin)
