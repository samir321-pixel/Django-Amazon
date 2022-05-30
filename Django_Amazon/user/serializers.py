from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models


class CoreRegisterSerializer(RegisterSerializer):
    is_amazon_admin = serializers.BooleanField(default=False)
    is_amazon_seller = serializers.BooleanField(default=False)
    is_amazon_customer = serializers.BooleanField(default=False)
    is_amazon_employee = serializers.BooleanField(default=False)
    is_amazon_delivery_service = serializers.BooleanField(default=False)
    is_amazon_proprietor = serializers.BooleanField(default=False)

    class Meta:
        model = models.User
        fields = ('email', 'username', 'password', 'is_amazon_admin', 'is_amazon_seller', 'is_amazon_delivery_service',
                  'is_amazon_customer', 'is_amazon_employee', 'is_amazon_proprietor' 'first_name')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'is_amazon_admin': self.validated_data.get('is_amazon_admin', ''),
            'is_amazon_customer': self.validated_data.get('is_amazon_customer', ''),
            'is_amazon_employee': self.validated_data.get('is_amazon_employee', ''),
            'is_amazon_seller': self.validated_data.get('is_amazon_seller', ''),
            'is_amazon_delivery_service': self.validated_data.get('is_amazon_delivery_service', ''),
            'is_amazon_proprietor': self.validated_data.get('is_amazon_proprietor', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_amazon_admin = self.cleaned_data.get('is_amazon_admin')
        user.is_amazon_customer = self.cleaned_data.get('is_amazon_customer')
        user.is_amazon_employee = self.cleaned_data.get('is_amazon_employee')
        user.is_amazon_seller = self.cleaned_data.get('is_amazon_seller')
        user.is_recruiter = self.cleaned_data.get('is_recruiter')
        user.is_amazon_delivery_service = self.cleaned_data.get('is_amazon_delivery_service')
        user.is_amazon_proprietor = self.cleaned_data.get('is_amazon_proprietor')
        user.first_name = self.cleaned_data.get('first_name')
        user.save()
        adapter.save_user(request, user, self)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('email', 'username', 'password', 'is_amazon_admin', 'is_amazon_customer', 'is_amazon_employee',
                  'is_amazon_delivery_service', 'is_amazon_proprietor', 'first_name', 'is_amazon_seller')


class ChangePasswordSerializer(serializers.Serializer):
    model = models.User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class TokenSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('key', 'user', 'user_type')

    def get_user_type(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        is_amazon_admin = serializer_data.get('is_amazon_admin')
        is_amazon_customer = serializer_data.get('is_amazon_customer')
        is_amazon_employee = serializer_data.get('is_amazon_employee')
        is_amazon_seller = serializer_data.get('is_amazon_seller')
        is_amazon_delivery_service = serializer_data.get('is_amazon_delivery_service')
        is_amazon_proprietor = serializer_data.get('is_amazon_proprietor')

        return {
            'is_amazon_admin': is_amazon_admin,
            'is_amazon_customer': is_amazon_customer,
            'is_amazon_employee': is_amazon_employee,
            'is_amazon_seller': is_amazon_seller,
            'is_amazon_delivery_service': is_amazon_delivery_service,
            'is_amazon_proprietor': is_amazon_proprietor,
        }
