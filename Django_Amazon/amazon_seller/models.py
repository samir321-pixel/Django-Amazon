from django.db import models
from phone_field import PhoneField
from localflavor.in_.models import INStateField
from djmoney.models.fields import MoneyField
from django.core.mail import send_mail

id_proof = (
    ("Aadhar Card", "Aadhar Card"),
    ("Pan Card", "Pan Card"),
)


# Create your models here.
class Amazon_Seller(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE, null=True, blank=True)
    unique_id = models.CharField(max_length=200, unique=True, editable=False, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    DOB = models.DateField()
    phone = PhoneField(blank=False, unique=True)
    alt_phone = PhoneField(blank=False)
    email = models.EmailField(unique=True)
    Address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = INStateField(null=True, blank=True)
    active=models.BooleanField(default=False)
    pincode = models.PositiveIntegerField(default=0)
    id_proof = models.CharField(max_length=30, choices=id_proof)
    id_proof_file = models.FileField(upload_to="media/Amazon_Sellers/id_proof_file")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    get_notified = models.BooleanField(default=True)
    password = models.CharField(max_length=300, null=True, blank=True, editable=False)
    qr_code = models.ImageField(upload_to='media/Amazon_Sellers/qr_codes', blank=True)

    def __str__(self):
        return "{}".format(self.first_name)


class Amazon_Seller_Notifications(models.Model):
    amazon_seller = models.ForeignKey(Amazon_Seller, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def seller_registered(self, amazon_seller, first_name, from_email, email):
        subject = "Register Successful"
        message = "Welcome {} being a part of Amazon Family. we will investigate your account and activate it".format(
            first_name)
        Amazon_Seller_Notifications.objects.create(amazon_seller=amazon_seller,
                                                   message=message)
        try:
            send_mail(subject, message, from_email, [email])
        except Exception as e:
            print("Failed to send Mail", e)

    def account_activated(self, amazon_seller, first_name, email, from_email, unique_id, password):
        subject = "Activated Successful"
        message = "Hi {}, your account is successfully activated here is your unique id {} and password {}".format(
            first_name, unique_id, password)
        Amazon_Seller_Notifications.objects.create(amazon_seller=amazon_seller,
                                                   message=message)
        try:
            send_mail(subject, message, from_email, [email])
        except Exception as e:
            print("Failed to send Mail", e)

    def account_deactivated(self, amazon_seller, first_name, email, from_email):
        subject = "Account Deactivated"
        message = "Hi {}, your account is deactivated. Thank you for your service".format(
            first_name)
        Amazon_Seller_Notifications.objects.create(amazon_seller=amazon_seller,
                                                   message=message)
        try:
            send_mail(subject, message, from_email, [email])
        except Exception as e:
            print("Failed to send Mail", e)

    # def mobile_details_registered(self, amazon_mobile, mobile_name, from_email, email):
    #     subject = "Mobile Details Register Successfully"
    #     message = "Hi {} Thanks for Ordering. We have received your order ".format(mobile_name)
    #     Amazon_Seller_Notifications.objects.create(amazon_mobile=amazon_mobile,
    #                                                message=message)
    #     try:
    #         send_mail(subject, message, from_email, [email])
    #     except Exception as e:
    #         print("Failed to send Mail", e)
