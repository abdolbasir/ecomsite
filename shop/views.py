from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.views import View
from .models import Product
# Create your views here.

class ProductsView(ListView):
    model = Product
    template_name ="shop/index.html"
    context_object_name = "products"
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        item_name = self.request.GET.get("item_name")
        if item_name != "" and item_name is not None:
            queryset = queryset.filter(title__icontains=item_name)
        return queryset
    
class ProductDetailView(DeleteView):
    model = Product
    template_name = "shop/product_detail.html"
    context_object_name = "product"

class CheckoutView(View):
     async def get(self, request):
        return render(request, "shop/checkout.html")

