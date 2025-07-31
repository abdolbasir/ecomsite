import json
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
        print(form.is_valid())
        if form.is_valid():
            items_str = form.cleaned_data['items']
            items = json.loads(items_str)
            total_price = 0
            for key in items:
                price_str = items[key]['price']
                price = float(price_str.replace("$", ""))
                quantity = int(items[key]['quantity'])
                total_price += price * quantity
            instance = form.save(commit=False)
            instance.total = total_price
            instance.save()
            return redirect('success') 
        
         # You can create this URL/template
        return render(request, self.template_name, {'form': form})


class SuccessView(View):
     template_name = 'shop/success.html'
     def get(self, request):
        return render(request, self.template_name)
    

