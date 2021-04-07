from .views import *
from django.urls import path, include


urlpatterns = [
    path('amazon_customer_signup/', Amazon_Customers_Signup_View.as_view()),
    path('amazon_customer_notification/', Amazon_Customer_Notification_View.as_view()),
]
