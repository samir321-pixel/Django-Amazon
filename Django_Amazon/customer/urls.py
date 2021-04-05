from .views import *
from django.urls import path, include


urlpatterns = [
    path('amazon_customer_signup/',Amazon_Customers_Signup_View.as_view()),
]
