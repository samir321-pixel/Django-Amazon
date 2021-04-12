from django.db import models
from django.db import models
from phone_field import PhoneField
from localflavor.in_.models import INStateField
from djmoney.models.fields import MoneyField
from django.core.mail import send_mail

gender_choices = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)
id_proof = (
    ("Aadhar Card", "Aadhar Card"),
    ("Pan Card", "Pan Card"),
)


class Amazon_Delivery_Service(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE, null=True, blank=True)
    unique_id = models.CharField(max_length=200, unique=True, editable=False, null=True, blank=True)
    service_name = models.CharField(max_length=200, unique=True)
    establish_date = models.DateField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    phone = PhoneField(blank=False, unique=True)
    alt_phone = PhoneField(blank=False)
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to="media/Amazon_Delivery_Service/profile")
    active = models.BooleanField(default=False)
    Address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = INStateField(null=True, blank=True)
    pincode = models.PositiveIntegerField(default=0)
    certificate = models.FileField(upload_to="media/Amazon_Delivery_Service/certificate")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    get_notified = models.BooleanField(default=True)
    password = models.CharField(max_length=300, null=False, blank=False)
    qr_code = models.ImageField(upload_to='media/Amazon_Delivery_Service/qr_codes', blank=True)

    def __str__(self):
        return "{}".format(self.service_name)


class Amazon_Delivery_Service_Notifications(models.Model):
    amazon_delivery_service = models.ForeignKey(Amazon_Delivery_Service, on_delete=models.CASCADE, null=True,
                                                blank=True)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def register_delivery_service(self, amazon_delivery_service, service_name, email, from_email):
        subject = "Register Successful"
        message = "Hi {} Thanks for registering. Your account is under reviewed we will get back to you soon!".format(
            service_name)
        Amazon_Delivery_Service_Notifications.objects.create(amazon_delivery_service=amazon_delivery_service,
                                                             message=message)
        try:
            send_mail(subject, message, from_email, [email])
        except Exception as e:
            print(e)
