from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug" : ["category_name"]
    }
    search_fields = ["category_name"]

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(ColorVarient)
class ColorVarientAdmin(admin.ModelAdmin):
    model = ColorVarient
    list_display = ["color_name"]

@admin.register(SizeVarient)
class SizeVarientAdmin(admin.ModelAdmin):
    model = SizeVarient
    list_display = ["size_name"]
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "price", "category"]
    prepopulated_fields = {
        "slug" : ["product_name"]
    }
    inlines = [ProductImageAdmin]
    autocomplete_fields = ["category"]
