from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsView.as_view(), name="index"),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name="product-detail")
]
