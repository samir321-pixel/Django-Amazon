from rest_framework import serializers
from .models import *


class Amazon_Employee_Signup_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Employee
        exclude = ["user", "unique_id", "id_proof_file", "qr_code", "get_notified", "active", "sallery",
                   "salary_due_date", "releasing_date"]


class Amazon_Employee_Notificartions_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Employee_Notifications
        fields = '__all__'
