from rest_framework import serializers
from .models import *


class Amazon_Admin_Signup_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Admin
        fields = ["first_name", "middle_name", "last_name", "DOB", "gender", "phone", "alt_phone", "email",
                  "profile_photo", "Address", "state", "pincode", "id_proof", "id_proof_file", "city", "password"]


class Amazon_Admin_Notificartions_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_admin_Notifications
        fields = '__all__'


class Amazon_Admin_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Admin
        fields = "__all__"


class Amazon_Admin_Update_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Admin
        exclude = ["id_proof", "profile_photo", "id_proof_file", "qr_code"]


class Amazon_Admin_Profile_Update_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Admin
        exclude = ["id_proof", "profile_photo", "id_proof_file", "qr_code"]
