from django.urls   import path

from product.views import ProductListView, ProductDetailView

urlpatterns = [
    path('/list/', ProductListView.as_view()),
    path('/detail/', ProductDetailView.as_view()),
]    
