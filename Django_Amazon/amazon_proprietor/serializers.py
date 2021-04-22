from rest_framework import serializers
from .models import *


class Amazon_Proprietor_Signup_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Proprietor
        exclude = ["user", "unique_id", "qr_code", "get_notified", "password"]
