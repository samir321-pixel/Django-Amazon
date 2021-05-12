from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics, status
from amazon_seller.models import Amazon_Seller
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.clickjacking import xframe_options_deny

class Amazon_Mobile_Create_View(generics.CreateAPIView):
    queryset = Amazon_Mobile.objects.all()
    serializer_class = Amazon_Mobile_Create_Serializer

    @xframe_options_deny
    def create(self, request, *args, **kwargs):
        if self.request.user.is_amazon_seller:
            try:
                amazon_seller_query = Amazon_Seller.objects.get(user=self.request.user)
            except ObjectDoesNotExist:
                return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
            if amazon_seller_query.active:
                serializer = self.get_serializer(data=self.request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.create(validated_data=request.data)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)

