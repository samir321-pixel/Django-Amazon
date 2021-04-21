from rest_framework import serializers
from .models import *


class Amazon_Seller_Signup_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Seller
        fields = ["first_name", "middle_name", "last_name", "DOB", "phone", "alt_phone", "email",
                  "Address", "city", "state", "pincode"]

class Amazon_Seller_Notificartions_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Seller_Notifications
        fields = '__all__'