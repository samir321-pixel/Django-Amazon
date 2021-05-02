from rest_framework import serializers
from .models import *


class Technology_Serializer(serializers.ModelSerializer):
    class Meta:
        model = mobile_technology
        fields = '__all__'


class Amazon_Mobile_Create_Serializer(serializers.HyperlinkedModelSerializer):
    technology = Technology_Serializer()

    class Meta:
        model = Amazon_Mobile
        fields = '__all__'
