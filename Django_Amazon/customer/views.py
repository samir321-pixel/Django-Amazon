from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from user.models import User
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin


class Amazon_Customers_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Customer.objects.all()
    serializer_class = Amazon_Customer_Signup_Serializer

    @xframe_options_sameorigin
    def perform_create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            user_query = User.objects.create_user(username=self.request.data['first_name'],
                                                  first_name=self.request.data['first_name'],
                                                  email=self.request.data['email'],
                                                  password=self.request.data['Password'],
                                                  last_name=self.request.data["last_name"],
                                                  is_amazon_customer=True)
            serializer.save(user=user_query)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class Amazon_Customer_Notification_View(generics.ListAPIView):
    queryset = Amazon_customers_Notifications.objects.all()
    serializer_class = Amazon_Customer_Notificartions_Serializer

    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_customer:
            customer_query = Amazon_Customer.objects.get(user=self.request.user)
            query = Amazon_customers_Notifications.objects.get(amazon_admin=customer_query)
            serializer = self.get_serializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
