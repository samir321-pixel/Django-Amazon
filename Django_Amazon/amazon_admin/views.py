from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, viewsets, status
from rest_framework.response import Response

from user.models import User


class Amazon_Admin_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Admin.objects.all()
    serializer_class = Amazon_Admin_Signup_Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print("This is First Name", self.request.data['first_name'])
        if serializer.is_valid(raise_exception=True):
            user_query = User.objects.create(username=self.request.data['first_name'],
                                             password=self.request.data["password"],
                                             first_name=self.request.data['first_name'],
                                             last_name=self.request.data["last_name"], is_amazon_admin=True)
            print("this is user query", user_query)
            serializer.save(user=user_query)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
