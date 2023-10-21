from django.contrib import admin
from .models import AD, Author, Category, Comment


def nullfy_quantity(modeladmin, request, queryset): 
    queryset.update(quantity=0)
nullfy_quantity.short_description = 'Обнулить товары'
class ADAdmin(admin.ModelAdmin):
    list_display = ('title', 'categoryType', 'dataCategory')
    list_filter = ['title', 'category']
    search_fields = ['title']
    actions = [nullfy_quantity]
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['authorUser']
    list_filter = ['authorUser']
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['NameCategory']
    search_fields = ['NameCategory']
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'commentUser']


    
admin.site.register(AD, ADAdmin)    
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)