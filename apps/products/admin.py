from django.contrib import admin

from apps.products.models import Product, Image


class ImageInline(admin.TabularInline):
    model = Product.images.through
    extra = 1


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image', ]
    list_display_links = ['image', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_display_links = ['title', ]
    list_filter = ['category', ]
    inlines = [ImageInline]
