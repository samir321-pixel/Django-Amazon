from .models import *
from django.shortcuts import render
from .serializers import *
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from user.models import User
from .utils import Unique_Name
from Django_Amazon.settings import EMAIL_HOST_USER

# Create your views here.
class Amazon_Delivery_Service_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Delivery_Service.objects.all()
    serializer_class = Amazon_Delivery_Service_Signup_Serializer

    def perform_create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            unique_id = Unique_Name()
            user_query = User.objects.create_user(username=unique_id,
                                                  first_name=self.request.data['first_name'],
                                                  email=self.request.data['email'],
                                                  password=self.request.data['password'],
                                                  last_name=self.request.data["last_name"],
                                                  is_amazon_employee=True)
            delivery_service_query = serializer.save(user=user_query, active=False, unique_id=unique_id,
                                             password=self.request.data['password'])
            Amazon_Delivery_Service_Notifications.Delivery_Service(self=self, amazon_Delivery_Service=delivery_service_query,
                                                              employee_name=delivery_service_query.first_name,
                                                              email=delivery_service_query.email, from_email=EMAIL_HOST_USER)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class Amazon_Delivery_Service_Notifications_View(generics.ListAPIView):
    queryset = Amazon_Delivery_Service_Notifications.objects.all()
    serializer_class = Amazon_Delivery_Service_Notifications_Serializer

    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_delivery_service:
            Delivery_Service = Amazon_Delivery_Service.objects.get(user=self.request.user)
            query = Amazon_Delivery_Service_Notifications.objects.get(amazon_Delivery_Service=Delivery_Service)
            serializer = self.get_serializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)