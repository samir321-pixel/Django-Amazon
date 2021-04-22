from rest_framework import serializers
from .models import *


class Amazon_Proprietor_Signup_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Proprietor
        fields = ["first_name", "middle_name", "last_name", "DOB", "phone", "alt_phone", "email",
                  "Address", "city", "state", "pincode"]


class Amazon_Proprietor_Notificartions_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Proprietor_Notifications
        fields = '__all__'


class Manage_Amazon_Proprietor_List_View_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Proprietor
        fields = "__all__"


class Amazon_Seller_Retrieve_Update_View_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Seller
        exclude = ["get_notified", "id_proof_file", "qr_code"]
