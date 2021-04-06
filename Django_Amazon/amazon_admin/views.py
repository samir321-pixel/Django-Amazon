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
            Amazon_admin_Notifications.admin_registered(self=self, amazon_admin=admin_query,
                                                        admin_name=admin_query.first_name)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class Amazon_Admin_Notification_View(generics.ListAPIView):
    queryset = Amazon_admin_Notifications.objects.all()
    serializer_class = Amazon_Admin_Notificartions_Serializer

    def list(self, request, *args, **kwargs):
        # user = self.request.user
        print(self.request.user, self.request.user.id)
        if self.request.user.is_amazon_admin:
            print("yes it is admin")
        else:
            print("its not admin")
        user_query = User.objects.get(id=self.request.user.id)
        query = Amazon_admin_Notifications.objects.all()
        serializer = self.get_serializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
