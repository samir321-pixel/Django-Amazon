from rest_framework import serializers
from .models import *
from user.model import User


class Amazon_Admin_Signup_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Admin
        field = "__all__"
