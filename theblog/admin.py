from django.contrib import admin
from .models import Post, Category, Profile, Comment,Postint,CategoryInt,Commentint

admin.site.register(Postint)
admin.site.register(Post)
admin.site.register(CategoryInt)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Commentint)