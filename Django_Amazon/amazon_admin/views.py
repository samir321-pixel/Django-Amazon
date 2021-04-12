from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from user.models import User
from .utils import Unique_Name, Unique_Password
from django.core.exceptions import ObjectDoesNotExist
from Django_Amazon.settings import EMAIL_HOST_USER
import datetime
import qrcode
from io import BytesIO
from PIL import Image, ImageDraw
from django.core.files import File


class Amazon_Admin_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Admin.objects.all()
    serializer_class = Amazon_Admin_Signup_Serializer

    def perform_create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            unique_id = Unique_Name()
            unique_password = Unique_Password()
            user_query = User.objects.create_user(username=unique_id,
                                                  first_name=self.request.data['first_name'],
                                                  email=self.request.data['email'],
                                                  password=unique_password,
                                                  last_name=self.request.data["last_name"],
                                                  is_amazon_admin=True)
            admin_query = serializer.save(user=user_query, active=False, unique_id=unique_id,
                                          password=unique_password)  # Amazon Admin
            try:
                qrcode_img = qrcode.make(self.request.data['first_name'] + "amazon_admin")
                canvas = Image.new('RGB', (290, 290), 'white')
                draw = ImageDraw.Draw(canvas)
                canvas.paste(qrcode_img)
                username = self.request.data['first_name']
                fname = f'amazon_code-{username}' + '.png'
                buffer = BytesIO()
                canvas.save(buffer, 'PNG')
                admin_query.qr_code.save(fname, File(buffer), save=True)
                canvas.close()
            except:
                pass
            Amazon_admin_Notifications.admin_registered(self=self, amazon_admin=admin_query,
                                                        admin_name=admin_query.first_name, email=admin_query.email,
                                                        from_email=EMAIL_HOST_USER)
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


class Manage_Amazon_Admin_ListView(generics.ListAPIView):
    queryset = Amazon_Admin.objects.all()
    serializer_class = Amazon_Admin_List_Serializer

    def list(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


class Manage_Amazon_Admin_Retrieve_View(generics.RetrieveUpdateAPIView):
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
                if serializer.validated_data.get('active'):
                    serializer.save(updated_at=datetime.datetime.now(), active=True)
                    Amazon_admin_Notifications.admin_activated(self=self, amazon_admin=instance,
                                                               amazon_admin_name=instance.first_name,
                                                               email=instance.email,
                                                               from_email=EMAIL_HOST_USER, password=instance.password,
                                                               unique_id=instance.unique_id)
                    return Response(serializer.data,
                                    status=status.HTTP_200_OK)  # Here is the solution of your yesterday prpblem!
                elif not serializer.validated_data.get('active'):
                    serializer.save(updated_at=datetime.datetime.now(), active=False)
                    Amazon_admin_Notifications.admin_deactivated(self=self, amazon_admin=instance,
                                                                 amazon_admin_name=instance.first_name,
                                                                 email=instance.email,
                                                                 from_email=EMAIL_HOST_USER)
                    return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


# create
# all
# update
# filter
# get


class Amazon_Admin_Profile_View(generics.RetrieveAPIView):
    queryset = Amazon_Admin.objects.all()
    serializer_class = Amazon_Admin_List_Serializer

    def retrieve(self, request, *args, **kwargs):
        if self.request.user.is_amazon_admin:
             #print("Log in user id is", self.request.user.id)
            user_query = User.objects.get(id=self.request.user.id)
            # print(user_query, "this is user query")
            admin_query = Amazon_Admin.objects.get(user=user_query)
            print(admin_query.active, "This says active")
            # print(admin_query, "Admin")
            if admin_query.active:
                serializer = self.get_serializer(admin_query)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


