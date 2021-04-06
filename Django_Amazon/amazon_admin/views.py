from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from user.models import User
from .utils import Unique_Name, Unique_Password


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
            admin_query = serializer.save(user=user_query)  # Amazon Admin
            Amazon_admin_Notifications.admin_registered(self=self, amazon_admin=admin_query, admin_name=)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
