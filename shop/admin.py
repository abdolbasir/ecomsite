from django.contrib import admin
from .models import Product, Order
from django.utils.html import format_html
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    
    def change_category_to_default(self,request,queryset):
        queryset.update(category="Default")

    change_category_to_default.short_description = "Make category default"
    list_display = ("title", "price", "discount_price","category", "description","image")
    search_fields = ("title",)
    actions = ('change_category_to_default',)
    list_editable = ("price", "discount_price",)

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "E-com Site"
admin.site.index_title = "Admin panel"
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)