from django.urls import path 

from product.views import SearchView

urlpatterns = [
    path('', SearchView.as_view()),
]
