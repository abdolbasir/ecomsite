from django.shortcuts import render,redirect
from django.views.generic import ListView, DeleteView
from django.views import View
from .models import Product
from .forms import OrderForm
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
     template_name = 'shop/checkout.html'
     def get(self, request):
        form = OrderForm()
        return render(request, self.template_name, {'form': form})
     
     def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # You can create this URL/template
        return render(request, self.template_name, {'form': form})


class SuccessView(View):
     template_name = 'shop/success.html'
     def get(self, request):
        return render(request, self.template_name)
    

