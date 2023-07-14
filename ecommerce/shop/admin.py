from django.contrib import admin

# Register your models here.
from shop.models import Category, Product


class Categoryadmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, Categoryadmin)


class Productadmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, Productadmin)
