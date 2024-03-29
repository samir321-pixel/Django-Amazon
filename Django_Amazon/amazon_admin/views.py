from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from user.models import User
from .utils import Unique_Name, Unique_Password
from django.core.exceptions import ObjectDoesNotExist

import datetime


class Amazon_Admin_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Admin.objects.all()
    serializer_class = Amazon_Admin_Signup_Serializer

    def perform_create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            user_query = User.objects.create_user(username=Unique_Name(),
                                                  first_name=self.request.data['first_name'],
                                                  email=self.request.data['email'],
                                                  password=Unique_Password(),
                                                  last_name=self.request.data["last_name"],
                                                  is_amazon_admin=True)
            admin_query = serializer.save(user=user_query, active=False)  # Amazon Admin
            Amazon_admin_Notifications.admin_registered(self=self, amazon_admin=admin_query,
                                                        admin_name=admin_query.first_name)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class Amazon_Admin_Notification_View(generics.ListAPIView):
    queryset = Amazon_admin_Notifications.objects.all()
    serializer_class = Amazon_Admin_Notificartions_Serializer

    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_admin:
            admin_query = Amazon_Admin.objects.get(user=self.request.user)
            query = Amazon_admin_Notifications.objects.get(amazon_admin=admin_query)
            serializer = self.get_serializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


class Amazon_Admin_ListView(generics.ListAPIView):
    queryset = Amazon_Admin.objects.all()
    serializer_class = Amazon_Admin_List_Serializer

    def list(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


class Amazon_Admin_Retrieve_View(generics.RetrieveUpdateAPIView):
    queryset = Amazon_Admin.objects.all()
    serializer_class = Amazon_Admin_Update_Serializer

    def retrieve(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            try:
                query = Amazon_Admin.objects.get(id=self.kwargs["id"])
                serializer = self.get_serializer(query)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


    def update(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            try:
                instance = Amazon_Admin.objects.get(id=self.kwargs["id"])
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
