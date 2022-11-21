from django.db import models
from django.contrib.auth.models import User
from home.models import Product
from userprofile.models import Profile

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title_g = models.CharField(max_length=50, blank=True, null=True, default='a')
    quantity = models.IntegerField()
    price = models.IntegerField()
    order_no = models.CharField(max_length=255)
    amount = models.IntegerField(null=True, blank=True)
    paid =  models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.title_r
    
    class Meta:
        db_table = 'cart'
        managed = True
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    paid = models.BooleanField()
    amount = models.IntegerField()
    phone = models.CharField(max_length=50)
    pay_code = models.CharField(max_length=100)
    shop_code = models.CharField(max_length=100)
    payment_date = models.DateTimeField(auto_now=True)
    admin_update = models.DateTimeField(auto_now_add=True)
    admin_note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Delivery(models.Model):
    GOLD = 'on delivery'
    SILVER = 'Online Payment'
    BRONZE = 'With card'

    MODE = [
        (GOLD, 'on delivery'),
        (BRONZE, 'With card'),
        ( SILVER,'Online Payment'),
    ]
    
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    payment_mode = models.CharField(max_length=50, default='on delivery', choices=MODE)
    
    