from django.db import models
from phone_field import PhoneField
from localflavor.in_.models import INStateField
from djmoney.models.fields import MoneyField

gender_choices = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)
id_proof = (
    ("Aadhar Card", "Aadhar Card"),
    ("Pan Card", "Pan Card"),
)


# Create your models here.
class Amazon_Admin(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE, null=True, blank=True)
    unique_id = models.CharField(max_length=200, unique=True, editable=False, null=True, blank=True)
    first_name = models.CharField(max_length=200, unique=True)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    DOB = models.DateField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    phone = PhoneField(blank=False, unique=True)
    alt_phone = PhoneField(blank=False)
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to="media/Amazon_Admins/profile")
    active = models.BooleanField(default=True)
    Address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = INStateField(null=True, blank=True)
    pincode = models.PositiveIntegerField(default=0)
    id_proof = models.CharField(max_length=30, choices=id_proof)
    id_proof_file = models.FileField(upload_to="media/Amazon_Admins/id_proof_file")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    get_notified = models.BooleanField(default=True)
    password = models.CharField(max_length=300, null=True, blank=True, unique=True, editable=False)
    qr_code = models.ImageField(upload_to='media/Amazon_Admins/qr_codes', blank=True)

    def __str__(self):
        return "{}".format(self.first_name)


class Amazon_admin_Notifications(models.Model):
    amazon_admin = models.ForeignKey(Amazon_Admin, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def admin_registered(self, amazon_admin, admin_name):
        message = "Congratulation you are now member of Amazon Service"
        Amazon_admin_Notifications.objects.create(amazon_admin=amazon_admin,
                                                  message=message)
        print("This is working")
