from django.http    import JsonResponse
from django.views   import View

from order.models   import Order, OrderStatus, OrderList
from user.models    import *
from product.models import *

class OrderListView(View):
    def post(self, request):
        data = json.loads(request.body)
        product = Prodcut.obejct.get(id=data['id'])
        order = Order.object.get(user=user)
        try:
            OrderList.objects.create(
                quantity=data['quantuty'],
                order = order,
                product = product,
            )
            return JsonResponse(status=200)
    def get(self, request):
        order = Orderlist.objects.get(user=user)

        return JsonResponse(status=200)