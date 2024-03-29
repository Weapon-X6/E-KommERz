from django.contrib import admin

from .models import Brand, Category, Product, ProductLine


class ProductLineInline(admin.TabularInline):
    model = ProductLine


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "category",
        "brand",
    ]
    inlines = [ProductLineInline]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


admin.site.register(Brand)
admin.site.register(
    Category,
)
admin.site.register(ProductLine)
