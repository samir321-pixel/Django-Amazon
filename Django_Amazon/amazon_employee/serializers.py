from rest_framework import serializers
from .models import *


class Amazon_Employee_Signup_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Employee
        fields = ["first_name", "middle_name", "last_name", "DOB", "gender", "phone", "alt_phone", "email",
                  "profile_photo", "Address", "state", "pincode", "id_proof", "id_proof_file", "city", "password"]


class Amazon_Employee_Notificartions_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Employee_Notifications
        fields = '__all__'
