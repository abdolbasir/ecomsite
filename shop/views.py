from django.views.generic import ListView
from .models import Product
# Create your views here.

class ProductsView(ListView):
    model = Product
    template_name ="shop/index.html"
    context_object_name = "products"