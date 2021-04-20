from .views import *
from django.urls import path, include

urlpatterns = [
    path('amazon_seller_signup/', Amazon_Seller_Signup_View.as_view()),
]