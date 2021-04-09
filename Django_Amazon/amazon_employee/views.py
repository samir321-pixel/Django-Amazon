from .models import *
from django.shortcuts import render
from .serializers import *
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from user.models import User
from .utils import Unique_Name, Unique_Password


# Create your views here.
#from ..user.models import User


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





            #user_query = User.objects.create_user(username=Unique_Name(),
                #                                  first_name=self.request.data['first_name'],
                 #                                 email=self.request.data['email'],
                  #                                password=Unique_Password(),
                   #                               last_name=self.request.data["last_name"],
                    #                              is_amazon_admin=True)
