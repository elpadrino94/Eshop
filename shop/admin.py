from django.contrib import admin

from shop.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "affliate_link", "created_at" )
    prepopulated_fields = {"slug": ('name',)}
    search_fields = ("name",)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

admin.site.register(Product, ProductAdmin),
admin.site.register(Category),
