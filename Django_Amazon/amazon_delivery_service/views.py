from .models import *
from django.shortcuts import render
from .serializers import *
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from user.models import User
from .utils import Unique_Name

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
            user_query = serializer.save(user=user_query, active=False, unique_id=unique_id,
                                             password=self.request.data['password'])
            #Amazon_Employee_Notifications.employee_registered(self=self, amazon_employee=employee_query,
                                                             # employee_name=employee_query.first_name,
                                                             # email=employee_query.email, from_email=EMAIL_HOST_USER)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
