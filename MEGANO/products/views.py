from django.http import JsonResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tag, Product, Review, Category
from .serializers import (
    ProductSerializer,
    ReviewSerializer,
    CategorySerializer,
    Catalog,
    CatalogSerializer,
)


class TagsView(APIView):
    def get(self, request: Request) -> JsonResponse:
        tags = Tag.objects.all().values()

        return JsonResponse(list(tags), safe=False)


class ProductView(APIView):
    def get(self, request: Request, **kwargs) -> Response:
        product = Product.objects.get(id=self.kwargs.get("id"))
        serializer = ProductSerializer(product, read_only=True)
        return Response(serializer.data)


class ProductReviewView(APIView):
    def post(self, request: Request, id):
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            review = serializer.save()
            product = Product.objects.get(id=id)
            product.reviews.add(review)
            reviews = product.reviews.all().values()
            return JsonResponse(list(reviews), safe=False)

        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BannersView(APIView):
    def get(self, request: Request) -> JsonResponse:
        products = Product.objects.all().values()
        return JsonResponse(list(products), safe=False)


class CategoriesView(APIView):
    def get(self, request: Request) -> Response:
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CatalogView(APIView):
    def get(self, request: Request) -> Response:
        products = Product.objects.all()

        print(self.kwargs['filter'])
        catalog = Catalog(products, currentPage=1, lastPage=2)
        serializer = CatalogSerializer(catalog)
        return Response(serializer.data)
