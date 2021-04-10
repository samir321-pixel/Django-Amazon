from .models import *
from django.shortcuts import render
from .serializers import *
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from user.models import User
from .utils import Unique_Name, Unique_Password
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


class Amazon_Employee_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Employee.objects.all()
    serializer_class = Amazon_Employee_Signup_Serializer

    def perform_create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class Amazon_Employee_Notification_View(generics.ListAPIView):
    queryset = Amazon_Employee_Notifications.objects.all()
    serializer_class = Amazon_Employee_Notificartions_Serializer

    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_employee:
            employee_query = Amazon_Employee.objects.get(user=self.request.user)
            query = Amazon_Employee_Notifications.objects.get(amazon_employee=employee_query)
            serializer = self.get_serializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
