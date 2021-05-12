from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from user.models import User
from amazon_admin.models import Amazon_Admin
from .utils import Unique_Name, Unique_Password
from django.core.exceptions import ObjectDoesNotExist
from Django_Amazon.settings import EMAIL_HOST_USER
import datetime
import qrcode
from io import BytesIO
from PIL import Image, ImageDraw
from django.core.files import File
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin


class Amazon_Seller_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Seller.objects.all()
    serializer_class = Amazon_Seller_Signup_Serializer

    @xframe_options_sameorigin
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
                                                  is_amazon_seller=True)
            seller_query = serializer.save(user=user_query, active=False, unique_id=unique_id,
                                           password=unique_password)
            try:
                qrcode_img = qrcode.make(self.request.data['first_name'] + "amazon_seller")
                canvas = Image.new('RGB', (290, 290), 'white')
                draw = ImageDraw.Draw(canvas)
                canvas.paste(qrcode_img)
                username = self.request.data['first_name']
                fname = f'amazon_code-{username}' + '.png'
                buffer = BytesIO()
                canvas.save(buffer, 'PNG')
                seller_query.qr_code.save(fname, File(buffer), save=True)
                canvas.close()
            except:
                pass
            Amazon_Seller_Notifications.seller_registered(self=self, amazon_seller=seller_query,
                                                          first_name=seller_query.first_name,
                                                          email=seller_query.email,
                                                          from_email=EMAIL_HOST_USER)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class Amazon_Seller_Notification_View(generics.ListAPIView):
    queryset = Amazon_Seller_Notifications.objects.all()
    serializer_class = Amazon_Seller_Notificartions_Serializer

    @xframe_options_sameorigin
    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_admin:
            seller_query = Amazon_Seller.objects.get(user=self.request.user)
            if seller_query.active:
                query = Amazon_Seller_Notifications.objects.get(amazon_seller=seller_query)
                serializer = self.get_serializer(query, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


class Manage_Amazon_Seller_List_View(generics.ListAPIView):
    queryset = Amazon_Seller.objects.all().order_by("-created_at")
    serializer_class = Amazon_Seller_List_View_Serializer

    @xframe_options_sameorigin
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


class Manage_Amazon_Seller_Retrieve_Update_View(generics.RetrieveUpdateAPIView):
    queryset = Amazon_Seller.objects.all()
    serializer_class = Amazon_Seller_Retrieve_Update_View_Serializer

    @xframe_options_sameorigin
    def retrieve(self, request, *args, **kwargs):
        if self.request.user.is_amazon_admin:
            try:
                query = Amazon_Seller.objects.get(id=self.kwargs["id"])
                serializer = self.get_serializer(query)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)

    @xframe_options_sameorigin
    def update(self, request, *args, **kwargs):
        if self.request.user.is_amazon_admin:
            try:
                instance = Amazon_Seller.objects.get(id=self.kwargs["id"])
            except ObjectDoesNotExist:
                return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.get_serializer(instance, data=self.request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                if serializer.validated_data.get('active'):
                    serializer.save(updated_at=datetime.datetime.now(), active=True)
                    Amazon_Seller_Notifications.account_activated(self=self, amazon_seller=instance,
                                                                  first_name=instance.first_name,
                                                                  email=instance.email,
                                                                  from_email=EMAIL_HOST_USER,
                                                                  password=instance.password,
                                                                  unique_id=instance.unique_id)
                    return Response(serializer.data,
                                    status=status.HTTP_200_OK)
                elif not serializer.validated_data.get('active'):
                    serializer.save(updated_at=datetime.datetime.now(), active=False)
                    Amazon_Seller_Notifications.account_deactivated(self=self, amazon_seller=instance,
                                                                    first_name=instance.first_name,
                                                                    email=instance.email,
                                                                    from_email=EMAIL_HOST_USER)
                    return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


class Amazon_Seller_Profile_View(generics.RetrieveUpdateAPIView):
    queryset = Amazon_Seller.objects.all()
    serializer_class = Amazon_Seller_List_View_Serializer

    @xframe_options_sameorigin
    def retrieve(self, request, *args, **kwargs):
        if self.request.user.is_amazon_seller:
            # Check it is active or not
            print("Log in user id is", self.request.user.id)
            user_query = User.objects.get(id=self.request.user.id)
            print(user_query, "this is user query")
            seller_query = Amazon_Seller.objects.get(user=user_query)
            print(seller_query, "Admin")
            serializer = self.get_serializer(seller_query)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)

    @xframe_options_sameorigin
    def update(self, request, *args, **kwargs):
        if self.request.user.is_amazon_seller:
            try:
                instance = Amazon_Seller.objects.get(id=self.kwargs["id"])
            except ObjectDoesNotExist:
                return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
            # Check it is active or not
            serializer = self.get_serializer(instance, data=self.request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(updated_at=datetime.datetime.now(), active=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
