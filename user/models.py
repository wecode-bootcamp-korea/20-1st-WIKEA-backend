from django.db import models

from product.models import Product 

class User(models.Model):
    email        = models.EmailField(max_length=128, unique=True)
    first_name   = models.CharField(max_length=32)
    last_name    = models.CharField(max_length=32)
    password     = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=32, unique=True)
    birthday     = models.CharField(max_length=32)
    create_at    = models.DateTimeField(auto_now_add=True)
    update_at    = models.DateTimeField(auto_now=True)
    wish_list    = models.ManyToManyField(Product, through="WishList")

    class Meta:
        db_table = "users"

class Order(models.Model):
    first_name   = models.CharField(max_length=32)
    last_name    = models.CharField(max_length=32)
    address      = models.CharField(max_length=128)
    sub_address  = models.CharField(max_length=128)
    user         = models.ForeignKey("User", on_delete=models.CASCADE)
    status       = models.ForeignKey("OrderStatus", on_delete=models.CASCADE)
    order_list   = models.ManyToManyField(Product, through="OrderList")

    class Meta:
        db_table = "orders"

class OrderStatus(models.Model):
    status       = models.CharField(max_length=32)

    class Meta:
        db_table = "order_status"

class OrderList(models.Model):
    quantity     = models.IntegerField(default=1)
    order        = models.ForeignKey("Order", on_delete=models.CASCADE)
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "order_lists"

class WishList(models.Model):
    user         = models.ForeignKey("User", on_delete=models.CASCADE)
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "wish_list"