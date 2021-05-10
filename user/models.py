from django.db import models

# Create your models here.
class Users(models.Model):
    email        = models.EmailField(max_length=128, unique=True)
    name         = models.CharField(max_length =32)
    password     = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=32, unique=True)
    birthday     = models.CharField(max_length=32)
    create_at    = models.DateTimeField(auto_now_add=True)
    update_at    = models.DateTimeField(auto_now =True)

    def Meta:
        db_table = "users"