from django.http    import JsonResponse
from django.views   import View

from user.utils     import authorize
from order.models   import Order, OrderStatus, OrderList, OrderStatus
from product.models import Product

class OrderListView(View): 
    @authorize
    def post(self, request): 
        data    = json.loads(request.body)
        user    = request.user
        product = Product.objects.filter(id=data['id']).values()
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

class OrderView(View):
    @authorize  
    def post(self, request):
        data  = json.loads(request.body)
        user  = request.user
        order = Order.objects.get(user=user)
        Order.objects.create(
            first_name  = data['first_name'],
            last_name   = data['last_name'],
            address     = data['adress'],
            sub_address = data['sub_adress'],
            user        = user,
            status      = OrderStatus.objects.get(id=1),
            order_list  = OrderList.objects.get(order=order),
        )
        return JsonResponse({'MASSAGE':'SUCCESS'}, status=200)
    
    @authorize
    def get(self, request):
        user = request.user
        if not Order.objects.filter(user=user).exists():
            return JsonResponse({'order':[]}, status=200)

        order = Order.objects.filter(user=user).values()
        return JsonResponse({'order':order}, status=200)