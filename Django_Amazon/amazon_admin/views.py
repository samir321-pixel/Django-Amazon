from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, viewsets, status
from rest_framework.response import Response


class Amazon_Admin_Signup_View(generics.CreateAPIView):
    queryset = Amazon_Admin.objects.all()
    serializer_class = Amazon_Admin_Signup_Serializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
