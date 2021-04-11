from .models import *
from django.shortcuts import render
from .serializers import *
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from user.models import User
from .utils import Unique_Name, Unique_Password
from django.core.exceptions import ObjectDoesNotExist
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File

# Create your views here.


class Amazon_Employee_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Employee.objects.all()
    serializer_class = Amazon_Employee_Signup_Serializer

    def perform_create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid(raise_exception=True):
            unique_id = Unique_Name()
            unique_password = Unique_Password()
            admin_query = User.objects.create_user(username=unique_id,
                                                  first_name=self.request.data['first_name'],
                                                  email=self.request.data['email'],
                                                  password=unique_password,
                                                  last_name=self.request.data["last_name"],
                                                  is_amazon_employee=True)
            employee_query = serializer.save(user=admin_query, active=False, unique_id=unique_id,
                                          password=unique_password)
            try:
                qrcode_img = qrcode.make(self.request.data['first_name'] + "amazon_employee")
                canvas = Image.new('RGB', (290, 290), 'white')
                draw = ImageDraw.Draw(canvas)
                canvas.paste(qrcode_img)
                username = self.request.data['first_name']
                fname = f'amazon_code-{username}' + '.png'
                buffer = BytesIO()
                canvas.save(buffer, 'PNG')
                employee_query.qr_code.save(fname, File(buffer), save=True)
                canvas.close()
            except:
                pass
            Amazon_Employee_Notifications.employee_registered(self=self, amazon_employee=employee_query,
                                                        employee_name=employee_query.first_name)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class Amazon_Employee_Notification_View(generics.ListAPIView):
    queryset = Amazon_Employee_Notifications.objects.all()
    serializer_class = Amazon_Employee_Notificartions_Serializer

    def list(self, request, *args, **kwargs):
        if self.request.user.is_amazon_employee:
            employee_query = Amazon_Employee.objects.get(user=self.request.user)
            query = Amazon_Employee_Notifications.objects.get(amazon_employee=employee_query)
            serializer = self.get_serializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"NO_ACCESS": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)
