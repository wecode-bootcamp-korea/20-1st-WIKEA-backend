import json

from django.views                 import View
from django.http                  import JsonResponse
from django.core.exceptions       import ValidationError

from product.models               import Product, SubCategory
from product.sub_product_queryset import get_queryset

class SearchView(View):
    def search(self, request):
        data = json.loads(request.body)
        
        products = [product.values() for product in Product.object.filter(korean_name__contain = data['korean_name'])

        return JsonResponse({'product':products}, status=200)


