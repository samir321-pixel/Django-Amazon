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
            amazon_seller=Amazon_Seller.objects.get(user=self.request.user)
            serializer.save(amazon_seller=amazon_seller)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class Amazon_Mobile_List_View(generics.ListAPIView):
    queryset = Amazon_Mobile.objects.all()
    serializer_class = Amazon_Mobile_Create_Serializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
