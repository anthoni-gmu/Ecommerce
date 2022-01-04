from django.urls import path

app_name="product"

from .views import (
    ProductDetailView,
    ListProductsView,
    ListSearchView,
    ListRelatedView,
    ListBySearchView,
)

urlpatterns = [
        path('product/<productId>',ProductDetailView.as_view()),
        path('get-products',ListProductsView.as_view()),
        path('search',ListSearchView.as_view()),
        path('related/<productId>',ListRelatedView.as_view()),
        path('by/search',ListBySearchView.as_view()),
]
