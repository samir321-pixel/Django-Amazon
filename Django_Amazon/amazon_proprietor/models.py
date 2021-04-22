from django.db import models
from phone_field import PhoneField
from localflavor.in_.models import INStateField

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
    password = models.CharField(max_length=300, null=True, blank=True, editable=False)
    qr_code = models.ImageField(upload_to='media/Amazon_Proprietor/qr_codes', blank=True)

    def __str__(self):
        return "{}".format(self.first_name)

