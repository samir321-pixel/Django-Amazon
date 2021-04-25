from django.db import models
from phone_field import PhoneField
from localflavor.in_.models import INStateField
from django.core.mail import send_mail

id_proof = (
    ("Aadhar Card", "Aadhar Card"),
    ("Pan Card", "Pan Card"),
)


# Create your models here.
class Amazon_Proprietor(models.Model):
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
    pincode = models.PositiveIntegerField(default=0)
    id_proof = models.CharField(max_length=30, choices=id_proof)
    id_proof_file = models.FileField(upload_to="media/Amazon_Proprietor/id_proof_file")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    get_notified = models.BooleanField(default=True)
    active = models.BooleanField(default=False)
    password = models.CharField(max_length=300, null=True, blank=True, editable=False)
    qr_code = models.ImageField(upload_to='media/Amazon_Proprietor/qr_codes', blank=True)
    profile = models.ImageField(upload_to='media/Amazon_Proprietor/profile', blank=True)

    def __str__(self):
        return "{}".format(self.first_name)





class Amazon_Proprietor_Notifications(models.Model):
    amazon_proprietor = models.ForeignKey(Amazon_Proprietor, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def register_amazon_proprietor(self, amazon_proprietor, first_name, email, from_email):
        subject = "Register Successful"
        message = "Hi {} Thanks for registering. Your account is under reviewed we will get back to you soon!".format(
            first_name)
        Amazon_Proprietor_Notifications.objects.create(amazon_proprietor=amazon_proprietor,
                                                       message=message)
        try:
            send_mail(subject, message, from_email, [email])
        except Exception as e:
            print("Failed to send Mail", e)

    def account_activated(self, amazon_proprietor, first_name, email, from_email, unique_id, password):
        subject = "Activated Successful"
        message = "Hi {}, your account is successfully activated here is your unique id {} and password {}".format(
            first_name, unique_id, password)
        Amazon_Proprietor_Notifications.objects.create(amazon_proprietor=amazon_proprietor,
                                                       message=message)
        try:
            send_mail(subject, message, from_email, [email])
        except Exception as e:
            print("Failed to send Mail", e)

    def account_deactivated(self, amazon_proprietor, first_name, email, from_email):
        subject = "Account Deactivated"
        message = "Hi {}, your account is deactivated. Thank you for your service".format(
            first_name)
        Amazon_Proprietor_Notifications.objects.create(amazon_proprietor=amazon_proprietor,
                                                       message=message)
        try:
            send_mail(subject, message, from_email, [email])
        except Exception as e:
            print("Failed to send Mail", e)
