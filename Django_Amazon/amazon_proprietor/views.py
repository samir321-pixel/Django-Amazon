import datetime
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from user.models import User
from .utils import Unique_Name, Unique_Password
from Django_Amazon.settings import EMAIL_HOST_USER
import qrcode
from io import BytesIO
from PIL import Image, ImageDraw
from django.core.files import File
from django.core.exceptions import ObjectDoesNotExist


class Amazon_Proprietor_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Proprietor.objects.all()
    serializer_class = Amazon_Proprietor_Signup_Serializer

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
            amazon_proprietor_query = serializer.save(user=user_query,  unique_id=unique_id,
                                                      password=password) #active=False,
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
