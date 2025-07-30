from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsView.as_view(), name="index"),
    path('checkout/', views.CheckoutView.as_view(), name ="checkout"),
    path('success/', views.SuccessView.as_view(), name="success"),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name="product-detail"),
   

]
