from django.urls import path
from .views import (
    ProductCreateView,
    ProductListView,
    ProductUpdateView,
    ProductDeleteView,
    ProductDetailView,
)

urlpatterns = [
    path("products/", ProductCreateView.as_view()),
    path("products/list/", ProductListView.as_view()),
    path("products/<int:pk>/", ProductDetailView.as_view()),
    path("products/<int:pk>/update/", ProductUpdateView.as_view()),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view()),
]