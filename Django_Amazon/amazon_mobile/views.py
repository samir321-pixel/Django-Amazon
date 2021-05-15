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
            tech = self.request.data.pop('mobile_technology')
            for i in tech:
                mobile_technology = Mobile_Technology.objects.create(**i)
                print(mobile_technology)
            # # print(album)
            # for techs in mobile_technology:
            #     print(techs)
            #     # mobile_technology.objects.create(**techs)
            return Response("ok")
        #
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
