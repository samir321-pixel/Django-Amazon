from rest_framework import serializers
from .models import *


class Amazon_Employee_Signup_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Employee
        fields = '__all__'
