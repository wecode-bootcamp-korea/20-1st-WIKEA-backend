from django.urls import path

from order.views import OrderListView

urlpatterns = [
    path('/shoppingcart/<str:korean_name>', OrderListView.as_view()),
]