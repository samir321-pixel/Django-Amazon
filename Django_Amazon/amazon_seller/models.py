from django.db import models
from phone_field import PhoneField
from localflavor.in_.models import INStateField
from djmoney.models.fields import MoneyField


# Create your models here.
class Amazon_Seller(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE, null=True, blank=True)
    seller_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    DOB = models.DateField()
    phone = PhoneField(blank=False, unique=True)
    alt_phone = PhoneField(blank=False)
    email = models.EmailField(unique=True)
    Address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = INStateField(null=True, blank=True)
    pincode = models.PositiveIntegerField(default=0)
    seller_code = models.IntegerField(default=0)
    seller_product_id = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    get_notified = models.BooleanField(default=True)
    password = models.CharField(max_length=300, null=True, blank=True, editable=False)

    def __str__(self):
        return "{}".format(self.seller_name)


class Amazon_Seller_Notifications(models.Model):
    amazon_seller = models.ForeignKey(Amazon_Seller, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    product_delivery = models.BooleanField()
    delivery_date = models.DateField()
    seller_product = models.CharField(max_length=100)
    seller_offers = models.CharField(max_length=200, default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def seller_registered(self, amazon_seller, seller_name):
        message = "Welcome {} being a part of Amazon Family".format(seller_name)
        Amazon_Seller_Notifications.objects.create(amazon_seller=amazon_seller,
                                                   message=message)
