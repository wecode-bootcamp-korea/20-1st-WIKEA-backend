import json

from django.views                 import View
from django.http                  import JsonResponse
from django.core.exceptions       import ValidationError
from djang.db.models              import Q

from product.models               import Product, SubCategory
from product.sub_product_queryset import get_queryset

class SearchView(View):
    def search(self, request):
        search = request.GET.get('search')
        if search:
            products = [product.values() for product in Product.object.filter(
                Q(korean_name__contain = search) & Q(english_name_contain = search) 
                &Q(sub_category__korean_name__contain = search) & Q(sub_category__english_name__contain = search) 
                &Q(category__korean_name__contain = search) & Q(category__korean_name__contatin = search))]

        return JsonResponse({'product':products}, status=200)


