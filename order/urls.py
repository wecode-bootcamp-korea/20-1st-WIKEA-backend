from django.urls import path

from order.view  import OrderView

urlpatterns = [
    path('/shoppingcart', OrderView.as_view()),
]