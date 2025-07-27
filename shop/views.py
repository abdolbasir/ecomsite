from django.views.generic import ListView
from .models import Product
# Create your views here.

class ProductsView(ListView):
    model = Product
    template_name ="shop/index.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = super().get_queryset()
        item_name = self.request.GET.get("item_name")
        if item_name != "" and item_name is not None:
            queryset = queryset.filter(title__icontains=item_name)
        return queryset