import json

from django.views                 import View
from django.http                  import JsonResponse
from django.core.exceptions       import ValidationError
from djang.db.models              import Q

from product.models               import Product
from product.sub_product_queryset import get_queryset

class SearchView(View):
    def search(self, request):
        search = request.GET.get('q')

        if search:
            products = [product.values() for product in Product.object.filter(
                Q(korean_name__contain = search) & Q(english_name_contain = search) 
                &Q(sub_category__korean_name__contain = search) & Q(sub_category__english_name__contain = search) 
                &Q(category__korean_name__contain = search) & Q(category__korean_name__contatin = search)
                &Q(series__korean_name__contain = search) & Q(series__english_name_contain = search)
                &Q(color__korean_name__contain = search) & Q(color__english_name_contain = search)).distinct()]

            result = [{
                        'korean_name'       : product.korean_name,
                        'english_name'      : product.english_name,
                        'price'             : product.price,
                        'special_price'     : product.special_price,
                        'is_new'            : product.is_new,
                        'color_list'        : [color.name for color in product.color.all()],
                        'image'             : [image.url for image in product.image.all()],
                        'series'            : series,
                    } for product in products]

        return JsonResponse({'product':result}, status=200)


