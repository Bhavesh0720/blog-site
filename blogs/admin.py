from django.contrib import admin
from .models import Category, Blog, SocialLinks, About, Comment

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'author', 'category', 'status', 'is_featured')
    search_fields = ('title', 'category__category_name', 'status')
    list_editable = ('is_featured',)
    list_filter = ('category__category_name', 'status')


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.count()
        if count == 0:
            return True
        return False


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(SocialLinks)
admin.site.register(Comment)
