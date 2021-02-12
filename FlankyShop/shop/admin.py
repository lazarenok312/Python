from django.contrib import admin

from .models import Category, Subcategory, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'subcategory', 'price', 'description', 'image']}),
    ]

    list_display = ('name', 'price', 'image', 'available', 'created', 'updated')
    list_filter = ['subcategory', 'price']
    list_editable = ['price', 'available']
    search_fields = ['subcategory', 'name', 'description']

class SubcategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'category', 'body']}),
    ]

    list_display = ('name', 'category', 'body')
    list_filter = ['category']
    search_fields = ['category', 'name', 'body']

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'body']}),
    ]

    list_display = ('name', 'body')
    search_fields = ['name', 'body']
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)