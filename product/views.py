import json

from django.views                 import View
from django.http                  import JsonResponse
from django.core.exceptions       import ValidationError
from django.db.models             import Q

from product.models               import Product

class SearchView(View):
    def get(self, request):
        try:
            search = request.GET.get('q')
            products = Product.objects.all()
            if search:
                products = products.filter(
                    Q(korean_name__contains = search) & Q(english_name__contains = search)
                    &Q(sub_category__korean_name__contain = search) & Q(sub_category__english_name__contain = search) 
                    &Q(category__korean_name__contain = search) & Q(category__korean_name__contatin = search)
                    &Q(series__korean_name__contain = search) & Q(series__english_name__contain = search)
                    &Q(color__korean_name__contain = search) & Q(color__english_name__contain = search))

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

                return JsonResponse({'search':result}, status=200)
            
        except Product.DoesNotExist:
            return JsonResponse({'search':'non-existent product'}, status=404)


