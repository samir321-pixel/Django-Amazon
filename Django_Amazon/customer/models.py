from django.db import models
from phone_field import PhoneField
from localflavor.in_.models import INStateField
from djmoney.models.fields import MoneyField

gender_choices = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)


# Create your models here.
class Amazon_Customer(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    DOB = models.DateField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    phone = PhoneField(blank=False, unique=True)
    alt_phone = PhoneField(blank=False)
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to="media/Amazon_Customers/profile")
    active = models.BooleanField(default=True)
    Address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = INStateField(null=True, blank=True)
    pincode = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    get_notified = models.BooleanField(default=True)
    password = models.CharField(max_length=300, null=True, blank=True, editable=False)

    def __str__(self):
        return "{}".format(self.first_name)


class Amazon_customers_Notifications(models.Model):
    amazon_customers = models.ForeignKey(Amazon_Customer, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    product_delivery = models.BooleanField()
    delivery_date = models.DateField()
    customer_product = models.CharField(max_length=100)
    amazon_offers = models.CharField(max_length=200, default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def customer_registered(self, amazon_customer, customer_name):
        message = "Congratulations {} being a part of Amazon Family".format(customer_name)
        Amazon_customers_Notifications.objects.create(amazon_customer=amazon_customer,
                                                      message=message)
