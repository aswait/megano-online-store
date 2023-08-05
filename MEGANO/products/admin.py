from django.contrib import admin

from .models import (
    Product,
    Specification,
    Tag,
    Image,
    Category,
    Review,
    Subcategory,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "category",
        "price",
        "count",
        "date",
        "title",
        "description",
        "fullDescription",
        "freeDelivery",
        "rating",
    ]


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "name",
        "value",
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "name",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "title",
        "image",
        "archived",
    ]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "title",
        "image",
        "archived",
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "src",
        "alt",
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "text",
        "rate",
        "date",
    ]
