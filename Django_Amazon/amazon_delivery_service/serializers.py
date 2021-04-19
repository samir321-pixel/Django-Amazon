from rest_framework import serializers
from .models import *


class Amazon_Delivery_Service_Signup_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Delivery_Service
        exclude = ["user", "unique_id", "qr_code", "get_notified", "active"]


class Amazon_Delivery_Service_Notifications_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Delivery_Service_Notifications
        fields = '__all__'


class Amazon_Delivery_Boy_Signup_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Delivery_Boy
        exclude = ["user", "unique_id", "qr_code", "get_notified", "active", "password"]


class Amazon_Delivery_Boy_Notifications_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Delivery_Boy_Notifications
        fields = '__all__'


class Amazon_Delivery_Service_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Delivery_Service
        exclude = ["qr_code", "get_notified", "password"]


class Amazon_Delivery_Service_Update_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Delivery_Service
        exclude = ["qr_code", "get_notified", "password", "profile_photo", "certificate"]


class Manage_Amazon_Delivery_Boy_List_View(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Delivery_Boy
        exclude = ["qr_code", "get_notified", "password", "profile_photo"]
