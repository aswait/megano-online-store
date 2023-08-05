from rest_framework import serializers

from .models import Tag, Image, Product, Category, Review, Specification, Subcategory


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ["name", "value"]


class ImageSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Image
        fields = ["src", "alt"]

    def get_src(self, obj):
        return obj.src.url


class SubcategorySerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = Subcategory
        fields = ["id", "title", "image"]


class CategorySerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "title", "image", "subcategories"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    tags = serializers.SerializerMethodField(read_only=True)
    reviews = ReviewSerializer(many=True)
    specifications = SpecificationSerializer(many=True)
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product

        fields = [
            "id",
            "category",
            "price",
            "count",
            "date",
            "title",
            "description",
            "fullDescription",
            "freeDelivery",
            "images",
            "tags",
            "reviews",
            "specifications",
            "rating",
        ]

    def get_tags(self, obj):
        print([tag.name for tag in obj.tags.all()])
        return [tag.name for tag in obj.tags.all()]

    def get_category(self, obj):
        return obj.category.title


class Catalog:
    def __init__(self, items, currentPage, lastPage):
        self.items = items
        self.lastPage = lastPage
        self.currentPage = currentPage


class CatalogSerializer(serializers.Serializer):
    items = ProductSerializer(many=True)
    currentPage = serializers.IntegerField()
    lastPage = serializers.IntegerField()

    class Meta:
        fields = ["items", "currentPage", "lastPage"]
