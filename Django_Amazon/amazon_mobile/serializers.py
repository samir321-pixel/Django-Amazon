from rest_framework import serializers
from .models import Amazon_Mobile, Mobile_Technology


class Technology_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile_Technology
        fields = ["technology_name"]


class Amazon_Mobile_Create_Serializer(serializers.ModelSerializer):
    # mobile_technology = Technology_Serializer(many=True)

    class Meta:
        model = Amazon_Mobile
        # fields = ["mobile_technology", "mobile_name"]
        fields = '__all__'


class Amazon_Mobile_List_Serializer(serializers.ModelSerializer):
    # mobile_technology = Technology_Serializer(many=True)

    class Meta:
        model = Amazon_Mobile
        fields = "__all__"
