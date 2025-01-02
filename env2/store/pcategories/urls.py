from django.urls import path
from .views import (
    CategoryAPIList, CategoryAPICreate, CategoryAPIDetail,
    ProductAPIList, ProductAPICreate, ProductAPIDetail
)

urlpatterns = [
    # Category URLs
    path('categories/', CategoryAPIList.as_view(), name='category-list'),
    path('categories/create/', CategoryAPICreate.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryAPIDetail.as_view(), name='category-detail'),

    # Product URLs
    path('products/', ProductAPIList.as_view(), name='product-list'),
    path('products/create/', ProductAPICreate.as_view(), name='product-create'),
    path('products/<slug:slug>/', ProductAPIDetail.as_view(), name='product-detail'),  # Use slug
]
