from .views import *
from django.urls import path, include

urlpatterns = [
    path('amazon_proprietor_signup/', Amazon_Proprietor_Signup_View.as_view()),
]