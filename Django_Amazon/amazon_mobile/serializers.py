from rest_framework import serializers
from .models import Amazon_Mobile, mobile_technology


class Technology_Serializer(serializers.ModelSerializer):
    class Meta:
        model = mobile_technology
        fields = "__all__"


class Amazon_Mobile_Create_Serializer(serializers.ModelSerializer):
    technology = Technology_Serializer(many=True)

    class Meta:
        model = Amazon_Mobile
        fields = ["technology", "mobile_name"]

    # def create(self, validated_data):
    #     print("Validated data : ", validated_data)
    #     technology = validated_data.pop('technology')
    #
    #     Amazon_Mobile = Amazon_Mobile.actions.create_initial(validated_data,technology )
    #     return Amazon_Mobile
