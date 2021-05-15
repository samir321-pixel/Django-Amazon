from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from user.models import User
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.views.decorators.clickjacking import xframe_options_deny


class Amazon_Customers_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Customer.objects.all()
    serializer_class = Amazon_Customer_Signup_Serializer

    @xframe_options_deny
    def perform_create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            user_query = User.objects.create_user(username=self.request.data['first_name'],
                                                  first_name=self.request.data['first_name'],
                                                  email=self.request.data['email'],
                                                  # password=self.request.data['Password'],
                                                  last_name=self.request.data["last_name"],
                                                  is_amazon_customer=True)
            serializer.save(user=user_query)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class Amazon_Customer_Notification_View(generics.ListAPIView):
    queryset = Amazon_customers_Notifications.objects.all()
    serializer_class = Amazon_Customer_Notificartions_Serializer

    @xframe_options_deny
    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_customer:
            customer_query = Amazon_Customer.objects.get(user=self.request.user)
            query = Amazon_customers_Notifications.objects.get(amazon_admin=customer_query)
            serializer = self.get_serializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)

class Amazon_Customer_ListView(generics.ListAPIView):
    queryset = Amazon_Customer.objects.all().order_by("-created_at")
    serializer_class = Amazon_Customer_List_Serializer

    @xframe_options_deny
    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_admin:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)

class Amazon_Customer_Profile_View(generics.RetrieveUpdateAPIView):
    queryset = Amazon_Customer.objects.all()
    serializer_class = Amazon_Customer_List_Serializer

    @xframe_options_deny
    def retrieve(self, request, *args, **kwargs):
        if self.request.user.is_amazon_admin:
            print("Log in user id is", self.request.user.id)
            user_query = User.objects.get(id=self.request.user.id)
            print(user_query, "this is user query")
            customer_query = Amazon_Customer.objects.get(user=user_query)
            print(customer_query, "Customer")
            if customer_query.active:
                serializer = self.get_serializer(customer_query)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)

    @xframe_options_deny
    def update(self, request, *args, **kwargs):
        if self.request.user.is_amazon_customer:
            try:
                instance = Amazon_Customer.objects.get(id=self.kwargs["id"])
            except ObjectDoesNotExist:
                return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.get_serializer(instance, data=self.request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(updated_at=datetime.datetime.now(), active=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
