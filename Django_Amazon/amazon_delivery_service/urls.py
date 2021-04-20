from .views import *
from django.urls import path, include

urlpatterns = [
    path('amazon_delivery_service_signup/', Amazon_Delivery_Service_Signup_View.as_view()),
    path('amazon_delivery_service_notification/', Amazon_Delivery_Service_Notifications_View.as_view()),
    path('amazon_delivery_boy_signup/', Amazon_Delivery_Boy_Signup_View.as_view()),
    path('amazon_delivery_boy_notification/', Amazon_Delivery_Boy_Notifications_View.as_view()),
    path('manage_amazon_delivery_service/', Manage_Amazon_Delivery_Service_ListView.as_view()),
    path('manage_amazon_delivery_service/<int:id>/', Manage_Amazon_Delivery_Service_Retrieve_View.as_view()),
    path('manage_amazon_delivery_boy/', Manage_Amazon_Delivery_Boy_List_View.as_view()),
    path('manage_amazon_delivery_boy/<int:id>/', Manage_Amazon_Delivery_Boy_Retrieve_View.as_view()),
]
