from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import DraggableMPTTAdmin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post)