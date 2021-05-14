from django.http    import JsonResponse
from django.views   import View

from user.utils     import authorize
from order.models   import Order, OrderStatus, OrderList
from user.models    import *
from product.models import *

class OrderListView(View): 
    @authorize
    def post(self, request): 
        data    = json.loads(request.body)
        user    = request.user
        product = Prodcut.objects.filter(id=data['id']).values()
        order   = Order.objects.get(user=user)
        try: 
            OrderList.objects.create(
                quantity = data['quantuty'],
                order    = order,
                product  = list(product),
            )
            return JsonResponse({'MASSAGE':'SUCCESS'}, status=200)

        except KeyError as e: 
            return JsonResponse({'MASSAGE':f'{e}'}, status=400)

    @authorize        
    def get(self, request): 
        product_list = OrderList.objects.all().product
        result       = []
        price        = 0
        for product in product_list: 
            result.append({product.name:list(Product.objects.filter(id=product).values())})
            if product.special_price != 0:
                price += product.special_price
            else: 
                price += product.price
        result.append({'total_price':price})    
        return JsonResponse({'result':result},status=200)
    
    @authorize
    def delete(request, korean_name): 
        user = request.body
        product = Product.objects.get(korean_name=korean_name)
        if not OrderList.objects.filter(product=product).exists(): 
            return JsonResponse({'MASSAGE':'Non-exists Product'}, status=400)
        order = OrderList.objects.filter(product=product)
        order.delete()
        return JsonResponse({'MASSAGE':'SUCCESS'}, status=200)

    @authorize
    def all_delete(request): 
        OrderList.objects.all().delete()    
        return JsonResponse({'MASSAGE':'SUCCESS'}, status=200)