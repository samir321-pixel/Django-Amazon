from .views import *
from django.urls import path, include

urlpatterns = [
    path('amazon_seller_signup/', Amazon_Seller_Signup_View.as_view()),
    path('amazon_seller_notification/', Amazon_Seller_Notification_View.as_view()),
    path('manage_amazon_seller/', Manage_Amazon_Seller_ListView.as_view()),
]