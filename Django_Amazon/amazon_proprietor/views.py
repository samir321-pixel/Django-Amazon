import datetime
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from user.models import User
from .utils import Unique_Name, Unique_Password, Delivery_Boy_Unique_Name, Delivery_Boy_Unique_Password
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
            amazon_proprietor_query = serializer.save(user=user_query, active=False, unique_id=unique_id,
                                                      password=password)

        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

