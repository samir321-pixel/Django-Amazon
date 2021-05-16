from rest_framework import serializers
from .models import Amazon_Mobile



class Amazon_Mobile_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon_Mobile
        fields = '__all__'


