from django.contrib import admin
from .models import Category, Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'author', 'category', 'status', 'is_featured')
    search_fields = ('title', 'category__category_name', 'status')
    list_editable = ('is_featured',)
    list_filter = ('category__category_name', 'status')

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
