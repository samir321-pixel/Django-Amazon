from .views import *
from django.urls import path, include

urlpatterns = [
    path('amazon_delivery_service_signup/', Amazon_Delivery_Service_Signup_View.as_view()),
]