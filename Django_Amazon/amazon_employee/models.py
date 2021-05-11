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




class Amazon_Employee(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE, null=True, blank=True)
    unique_id = models.CharField(max_length=200, unique=True, editable=False, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    DOB = models.DateField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    phone = PhoneField(blank=False, unique=True)
    alt_phone = PhoneField(blank=False)
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to="media/Amazon_Employee/profile")
    active = models.BooleanField(default=False)
    Address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = INStateField(null=True, blank=True)
    pincode = models.PositiveIntegerField(default=0)
    id_proof = models.CharField(max_length=30, choices=id_proof)
    id_proof_file = models.FileField(upload_to="media/Amazon_Employee/id_proof_file")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    get_notified = models.BooleanField(default=True)
    password = models.CharField(max_length=300, null=True, blank=True, unique=True, editable=False)
    qr_code = models.ImageField(upload_to='media/Amazon_Employee/qr_codes', blank=True)
    sallery = MoneyField(default=0, default_currency='INR', max_digits=11, null=True, blank=True)
    salary_due_date = models.DateField(blank=True, null=True)
    releasing_date = models.DateField(null=True, blank=True)
    Resume = models.FileField(upload_to="media/Amazon_Employee/resume_file")
    Past_Experince = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.first_name)


class Amazon_Employee_Notifications(models.Model):
    amazon_employee = models.ForeignKey(Amazon_Employee, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def employee_registered(self, amazon_employee, employee_name, from_email, email):
        subject = "Register Successful"
        message = "Welcome {} Now, you are employee of Amazon Service. Your account will be activated soon.".format(
            employee_name)
        Amazon_Employee_Notifications.objects.create(amazon_employee=amazon_employee,
                                                     message=message)
        try:
            send_mail(subject, message, from_email, [email])
        except Exception as e:
            print("Error capture here", e)

    def employee_activated(self, amazon_employee, amazon_employee_name, email, from_email, unique_id, password):
        subject = "Activated Successful"
        message = "Hi {}, your account is successfully activated here is your unique id {} and password {}".format(
            amazon_employee_name, unique_id, password)
        Amazon_Employee_Notifications.objects.create(amazon_employee=amazon_employee, message=message)
        try:
            send_mail(subject, message, from_email, [email])
        except Exception as e:
            print(e)

    def employee_deactivated(self, amazon_employee, amazon_employee_name, email, from_email):
        subject = "Accound Deactivated"
        message = "Hi {}, your account is deactivated. Thank you for your service".format(
            amazon_employee_name)
        Amazon_Employee_Notifications.objects.create(amazon_employee=amazon_employee, message=message)
        try:
            send_mail(subject, message, from_email, [email])
        except:
            pass



