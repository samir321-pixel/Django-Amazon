from .views import *
from django.urls import path, include

urlpatterns = [
    path('amazon_delivery_service_signup/', Amazon_Delivery_Service_Signup_View.as_view()),
    path('amazon_delivery_service_notification/', Amazon_Delivery_Service_Notifications_View.as_view())
    #path('amazon_delivery_boy_signup/', Amazon_Delivery_Boy_Signup_View.as_view())

]