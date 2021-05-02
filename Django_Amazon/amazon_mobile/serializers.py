from rest_framework import serializers
from .models import *


class Technology_Serializer(serializers.ModelSerializer):
    class Meta:
        model = mobile_technology
        fields = '__all__'


class Amazon_Mobile_Create_Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Amazon_Mobile
        exclude = ['amazon_seller']

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        tech_data = validated_data.pop('mobile_technology')
        tech = Technology_Serializer.create(Technology_Serializer(), validated_data=tech_data)
        mobile, created = Amazon_Mobile.objects.update_or_create(mobile_technology=tech)
        return mobile
