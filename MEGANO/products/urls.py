from django.urls import path

from .views import (
    TagsView,
    ProductView,
    ProductReviewView,
    BannersView,
    CategoriesView,
    CatalogView,
)


urlpatterns = [
    path("tags", TagsView.as_view(), name="tags"),
    path("catalog", CatalogView.as_view(), name="catalog"),
    path("categories", CategoriesView.as_view(), name="categories"),
    path("product/<int:id>", ProductView.as_view(), name="product"),
    path("product/<int:id>/reviews", ProductReviewView.as_view(), name="product_review"),
]
