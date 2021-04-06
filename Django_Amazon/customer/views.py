from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from user.models import User
from .utils import Unique_Name, Unique_Password


class Amazon_Customers_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Customer.objects.all()
    serializer_class = Amazon_Customer_Signup_Serializer

    def perform_create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            user_query = User.objects.create_user(username=self.request.data['first_name'],
                                                  first_name=self.request.data['first_name'],
                                                  email=self.request.data['email'],
                                                  password=self.request.data['Password'],
                                                  last_name=self.request.data["last_name"],
                                                  is_amazon_admin=True)
            serializer.save(user=user_query)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
