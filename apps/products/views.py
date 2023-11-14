from typing import Any
from django.views.generic import ListView
from apps.products.models import Product
from apps.categories.models import Category


class ProductListView(ListView):
    model = Product
    template_name = "products/shop-sidebar.html"
    context_object_name = "products"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        context['categories'] = Category.objects.all()
        
        return context
        
