from django.contrib import admin
from .models import PostModel

# Register your models here.
@admin.register(PostModel)
class UserAdmin(admin.ModelAdmin):
    model = PostModel
    list_display = ['title']
