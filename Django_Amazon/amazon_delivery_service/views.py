from .models import *
import datetime
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from user.models import User
from amazon_admin.models import Amazon_Admin
from .utils import Unique_Name, Unique_Password, Delivery_Boy_Unique_Name, Delivery_Boy_Unique_Password
from Django_Amazon.settings import EMAIL_HOST_USER
import qrcode
from io import BytesIO
from PIL import Image, ImageDraw
from django.core.files import File
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin


# Create your views here.
class Amazon_Delivery_Service_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Delivery_Service.objects.all()
    serializer_class = Amazon_Delivery_Service_Signup_Serializer

    @xframe_options_sameorigin
    def perform_create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            unique_id = Unique_Name()
            password = Unique_Password()
            user_query = User.objects.create_user(username=unique_id,
                                                  first_name=self.request.data['service_name'],
                                                  email=self.request.data['email'],
                                                  password=password,
                                                  is_amazon_delivery_service=True)
            delivery_service_query = serializer.save(user=user_query, active=False, unique_id=unique_id,
                                                     password=password)
            try:
                qrcode_img = qrcode.make(self.request.data['first_name'] + "amazon_delivery_service")
                canvas = Image.new('RGB', (290, 290), 'white')
                draw = ImageDraw.Draw(canvas)
                canvas.paste(qrcode_img)
                username = self.request.data['first_name']
                fname = f'amazon_delivery_service_code-{username}' + '.png'
                buffer = BytesIO()
                canvas.save(buffer, 'PNG')
                delivery_service_query.qr_code.save(fname, File(buffer), save=True)
                canvas.close()
            except:
                pass
            Amazon_Delivery_Service_Notifications.register_delivery_service(self=self,
                                                                            amazon_delivery_service=delivery_service_query,
                                                                            service_name=delivery_service_query.service_name,
                                                                            email=delivery_service_query.email,
                                                                            from_email=EMAIL_HOST_USER)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class Amazon_Delivery_Service_Notifications_View(generics.ListAPIView):
    queryset = Amazon_Delivery_Service_Notifications.objects.all()
    serializer_class = Amazon_Delivery_Service_Notifications_Serializer

    @xframe_options_sameorigin
    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_delivery_service:
            delivery_service_query = Amazon_Delivery_Service.objects.get(user=self.request.user)
            if delivery_service_query.active:
                query = Amazon_Delivery_Service_Notifications.objects.get(
                    amazon_delivery_service=delivery_service_query)
                serializer = self.get_serializer(query, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


class Amazon_Delivery_Boy_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Delivery_Boy.objects.all()
    serializer_class = Amazon_Delivery_Boy_Signup_Serializer

    @xframe_options_sameorigin
    def perform_create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            unique_id = Delivery_Boy_Unique_Name()
            password = Delivery_Boy_Unique_Password()
            user_query = User.objects.create_user(username=unique_id,
                                                  first_name=self.request.data['first_name'],
                                                  email=self.request.data['email'],
                                                  password=password, is_amazon_delivery_service_boy=True)
            delivery_boy_query = serializer.save(user=user_query, active=False, unique_id=unique_id,
                                                 password=password)
            try:
                qrcode_img = qrcode.make(self.request.data['first_name'] + "amazon_delivery_boy")
                canvas = Image.new('RGB', (290, 290), 'white')
                draw = ImageDraw.Draw(canvas)
                canvas.paste(qrcode_img)
                username = self.request.data['first_name']
                fname = f'amazon_delivery_boy_code-{username}' + '.png'
                buffer = BytesIO()
                canvas.save(buffer, 'PNG')
                delivery_boy_query.qr_code.save(fname, File(buffer), save=True)
                canvas.close()
            except:
                pass
            Amazon_Delivery_Boy_Notifications.register_delivery_boy(self=self,
                                                                    amazon_delivery_boy=delivery_boy_query,
                                                                    amazon_delivery_boy_name=delivery_boy_query,
                                                                    email=delivery_boy_query.email,
                                                                    from_email=EMAIL_HOST_USER)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class Amazon_Delivery_Boy_Notifications_View(generics.ListAPIView):
    queryset = Amazon_Delivery_Boy_Notifications.objects.all()
    serializer_class = Amazon_Delivery_Boy_Notifications_Serializer

    @xframe_options_sameorigin
    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_delivery_service:
            delivery_service_boy_query = Amazon_Delivery_Boy.objects.get(user=self.request.user)
            if delivery_service_boy_query.active:
                query = Amazon_Delivery_Boy_Notifications.objects.get(
                    amazon_delivery_boy=delivery_service_boy_query)
                serializer = self.get_serializer(query, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


class Manage_Amazon_Delivery_Service_ListView(generics.ListAPIView):
    queryset = Amazon_Delivery_Service.objects.all().order_by("-created_at")
    serializer_class = Amazon_Delivery_Service_List_Serializer

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


class Manage_Amazon_Delivery_Service_Retrieve_View(generics.RetrieveUpdateAPIView):
    queryset = Amazon_Delivery_Service.objects.all()
    serializer_class = Amazon_Delivery_Service_Update_Serializer

    @xframe_options_sameorigin
    def retrieve(self, request, *args, **kwargs):
        if self.request.user.is_amazon_admin:
            try:
                query = Amazon_Delivery_Service.objects.get(id=self.kwargs["id"])
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
                instance = Amazon_Delivery_Service.objects.get(id=self.kwargs["id"])
            except ObjectDoesNotExist:
                return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.get_serializer(instance, data=self.request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                if serializer.validated_data.get('active'):
                    serializer.save(updated_at=datetime.datetime.now(), active=True)
                    Amazon_Delivery_Service_Notifications.account_activated(self=self, amazon_delivery_service=instance,
                                                                            service_name=instance.service_name,
                                                                            email=instance.email,
                                                                            from_email=EMAIL_HOST_USER,
                                                                            password=instance.password,
                                                                            unique_id=instance.unique_id)
                    return Response(serializer.data,
                                    status=status.HTTP_200_OK)
                elif not serializer.validated_data.get('active'):
                    serializer.save(updated_at=datetime.datetime.now(), active=False)
                    Amazon_Delivery_Service_Notifications.account_deactivated(self=self,
                                                                              amazon_delivery_service=instance,
                                                                              service_name=instance.service_name,
                                                                              email=instance.email,
                                                                              from_email=EMAIL_HOST_USER)
                    amazon_delivery_boy_query = Amazon_Delivery_Boy.objects.filter(active=True,
                                                                                   amazon_deliery_service=instance.id)
                    # print("Delivery", amazon_delivery_boy_query)
                    for x in amazon_delivery_boy_query:
                        print("boy is", x, "he is", )

                    return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


class Manage_Amazon_Delivery_Boy_List_View(generics.ListAPIView):
    queryset = Amazon_Delivery_Boy.objects.all().order_by("-created_at")
    serializer_class = Manage_Amazon_Delivery_Boy_List_View_Serializer

    @xframe_options_sameorigin
    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_delivery_service:
            amazon_delivery_service_query = Amazon_Delivery_Service.objects.get(user=self.request.user)
            if amazon_delivery_service_query.active:
                query = Amazon_Delivery_Boy.objects.filter(
                    amazon_deliery_service=Amazon_Delivery_Service.objects.get(user=self.request.user.id))
                serializer = self.get_serializer(query, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


class Manage_Amazon_Delivery_Boy_Active_List_View(generics.ListAPIView):
    queryset = Amazon_Delivery_Boy.objects.filter(active=True)
    serializer_class = Manage_Amazon_Delivery_Boy_List_View_Serializer

    @xframe_options_sameorigin
    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_delivery_service:
            amazon_delivery_service_query = Amazon_Delivery_Service.objects.get(user=self.request.user)
            if amazon_delivery_service_query.active:
                amazon_delivery_boy_query = Amazon_Delivery_Boy.objects.filter(active=True,
                                                                               amazon_deliery_service=amazon_delivery_service_query)
                serializer = self.get_serializer(amazon_delivery_boy_query, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


class Manage_Amazon_Delivery_Boy_Deactive_List_View(generics.ListAPIView):
    queryset = Amazon_Delivery_Boy.objects.filter(active=False)
    serializer_class = Manage_Amazon_Delivery_Boy_List_View_Serializer

    @xframe_options_sameorigin
    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_delivery_service:
            amazon_delivery_service_query = Amazon_Delivery_Service.objects.get(user=self.request.user)
            if amazon_delivery_service_query.active:
                amazon_delivery_boy_query = Amazon_Delivery_Boy.objects.filter(active=False,
                                                                               amazon_deliery_service=amazon_delivery_service_query)
                serializer = self.get_serializer(amazon_delivery_boy_query, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)


class Manage_Amazon_Delivery_Boy_Retrieve_View(generics.RetrieveUpdateAPIView):
    queryset = Amazon_Delivery_Service.objects.all()
    serializer_class = Manage_Amazon_Delivery_Boy_Update_View_Serializer

    @xframe_options_sameorigin
    def retrieve(self, request, *args, **kwargs):
        if self.request.user.is_amazon_delivery_service:
            amazon_delivery_service_query = Amazon_Delivery_Service.objects.get(user=self.request.user.id)
            if amazon_delivery_service_query.active:
                try:
                    query = Amazon_Delivery_Boy.objects.get(id=self.kwargs["id"])
                    serializer = self.get_serializer(query)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except ObjectDoesNotExist:
                    return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)

    @xframe_options_sameorigin
    def update(self, request, *args, **kwargs):
        if self.request.user.is_amazon_delivery_service:
            amazon_delivery_service_query = Amazon_Delivery_Service.objects.get(user=self.request.user.id)
            if amazon_delivery_service_query.active:
                try:
                    query = Amazon_Delivery_Boy.objects.get(id=self.kwargs["id"])
                    serializer = self.get_serializer(query, data=self.request.data, partial=True)
                    if serializer.is_valid(raise_exception=True):
                        if serializer.validated_data.get('active'):
                            serializer.save(updated_at=datetime.datetime.now(), active=True)
                            Amazon_Delivery_Boy_Notifications.account_activated(self=self,
                                                                                amazon_delivery_boy=query,
                                                                                amazon_delivery_boy_name=query.first_name,
                                                                                email=query.email,
                                                                                from_email=EMAIL_HOST_USER,
                                                                                password=query.password,
                                                                                unique_id=query.unique_id)
                            return Response(serializer.data, status=status.HTTP_200_OK)
                        elif not serializer.validated_data.get('active'):
                            serializer.save(updated_at=datetime.datetime.now(), active=False)
                            Amazon_Delivery_Boy_Notifications.account_deactivated(self=self,
                                                                                  amazon_delivery_boy=query,
                                                                                  amazon_delivery_boy_name=query.first_name,
                                                                                  email=query.email,
                                                                                  from_email=EMAIL_HOST_USER)
                            return Response(serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
                except ObjectDoesNotExist:
                    return Response({"DOES_NOT_EXIST": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
