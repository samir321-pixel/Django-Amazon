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
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            print(self.request.data)
            tech = self.request.data.pop('mobile_technology')
            for i in tech:
                mobile_technology = Mobile_Technology.objects.create(**i)
                print(mobile_technology)
            amazon_mobile = Amazon_Mobile.objects.create(**self.request.data, mobile_technology=mobile_technology)
            # mobile_technology = Mobile_Technology.objects.create(**self.request.data)
            # print(mobile_technology)
            # tech = self.request.data.pop('mobile_technology')
            # for i in tech:
            #     mobile_technology = Mobile_Technology.objects.create(amazon_mobile=amazon_mobile, **i)
            #     print(mobile_technology)
            # # print(album)
            # for techs in mobile_technology:
            #     print(techs)
            #     # mobile_technology.objects.create(**techs)
            return Response("Ok")
        #
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class Amazon_Mobile_List_View(generics.ListAPIView):
    queryset = Mobile_Technology.objects.all()
    serializer_class = Amazon_Mobile_List_Serializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
