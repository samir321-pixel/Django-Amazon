from rest_framework import serializers
from .models import *


class Amazon_Admin_Signup_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Admin
        fields = "__all__"
