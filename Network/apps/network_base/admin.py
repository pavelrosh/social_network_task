from django.contrib import admin
from . models import User, Post

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields[1:]]
    search_fields = [field.name for field in User._meta.fields]
    list_filter = [field.name for field in User._meta.fields]


admin.site.register(User, UserAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields[1:]]
    search_fields = [field.name for field in Post._meta.fields]
    list_filter = [field.name for field in Post._meta.fields]


admin.site.register(Post, PostAdmin)
