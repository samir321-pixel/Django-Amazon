import datetime
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from user.models import User
from amazon_admin.models import Amazon_Admin
from .utils import Unique_Name, Unique_Password
from Django_Amazon.settings import EMAIL_HOST_USER
import qrcode
from io import BytesIO
from PIL import Image, ImageDraw
from django.core.files import File
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin


class Amazon_Proprietor_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Proprietor.objects.all()
    serializer_class = Amazon_Proprietor_Signup_Serializer

    @xframe_options_sameorigin
    def perform_create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            unique_id = Unique_Name()
            password = Unique_Password()
            user_query = User.objects.create_user(username=unique_id,
                                                  first_name=self.request.data['first_name'],
                                                  email=self.request.data['email'],
                                                  password=password,
                                                  is_amazon_proprietor=True)
            amazon_proprietor_query = serializer.save(user=user_query, active=False, unique_id=unique_id,
                                                      password=password)  # active=False,
            try:
                qrcode_img = qrcode.make(self.request.data['first_name'] + "amazon_proprietor")
                canvas = Image.new('RGB', (290, 290), 'white')
                draw = ImageDraw.Draw(canvas)
                canvas.paste(qrcode_img)
                username = self.request.data['first_name']
                fname = f'amazon_proprietor_code-{username}' + '.png'
                buffer = BytesIO()
                canvas.save(buffer, 'PNG')
                amazon_proprietor_query.qr_code.save(fname, File(buffer), save=True)
                canvas.close()
            except:
                pass
            Amazon_Proprietor_Notifications.register_amazon_proprietor(self=self,
                                                                       amazon_proprietor=amazon_proprietor_query,
                                                                       first_name=amazon_proprietor_query.first_name,
                                                                       email=amazon_proprietor_query.email,
                                                                       from_email=EMAIL_HOST_USER)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class Amazon_Proprietor_Notifications_View(generics.ListAPIView):
    queryset = Amazon_Proprietor_Notifications.objects.all()
    serializer_class = Amazon_Proprietor_Notifications_Serializer

    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_admin:
            amazon_proprietor_query = Amazon_Proprietor.objects.get(user=self.request.user)
            if amazon_proprietor_query.active:
                query = Amazon_Proprietor_Notifications.objects.get(
                    amazon_proprietor=amazon_proprietor_query)
                serializer = self.get_serializer(query, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


class Manage_Amazon_Proprietor_List_View(generics.ListAPIView):
    queryset = Amazon_Proprietor.objects.all().order_by("-created_at")
    serializer_class = Amazon_Proprietor_List_Serializer

    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_admin:
            amazon_admin_query = Amazon_Admin.objects.get(user=self.request.user.id)
            if amazon_admin_query.active:
                serializer = self.get_serializer(self.get_queryset(), many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


class Manage_Amazon_Proprietor_Retrieve_Update_View(generics.RetrieveUpdateAPIView):
    queryset = Amazon_Proprietor.objects.all()
    serializer_class = Amazon_Proprietor_Retrieve_Update_View_Serializer

    def retrieve(self, request, *args, **kwargs):
        if self.request.user.is_amazon_admin:
            try:
                query = Amazon_Proprietor.objects.get(id=self.kwargs["id"])
                serializer = self.get_serializer(query)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        if self.request.user.is_amazon_admin:
            try:
                instance = Amazon_Proprietor.objects.get(id=self.kwargs["id"])
            except ObjectDoesNotExist:
                return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.get_serializer(instance, data=self.request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                if serializer.validated_data.get('active'):
                    serializer.save(updated_at=datetime.datetime.now(), active=True)
                    Amazon_Proprietor_Notifications.account_activated(self=self, amazon_proprietor=instance,
                                                                      first_name=instance.first_name,
                                                                      email=instance.email,
                                                                      from_email=EMAIL_HOST_USER,
                                                                      password=instance.password,
                                                                      unique_id=instance.unique_id)
                    return Response(serializer.data,
                                    status=status.HTTP_200_OK)
                elif not serializer.validated_data.get('active'):
                    serializer.save(updated_at=datetime.datetime.now(), active=False)
                    Amazon_Proprietor_Notifications.account_deactivated(self=self, amazon_proprietor=instance,
                                                                        first_name=instance.first_name,
                                                                        email=instance.email,
                                                                        from_email=EMAIL_HOST_USER)
                    return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
