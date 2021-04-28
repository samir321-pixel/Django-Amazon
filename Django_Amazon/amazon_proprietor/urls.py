from .views import *
from django.urls import path, include

urlpatterns = [
    path('amazon_proprietor_signup/', Amazon_Proprietor_Signup_View.as_view()),
    path('amazon_proprietor_notification/', Amazon_Proprietor_Notifications_View.as_view()),
    path('manage_amazon_proprietor/', Manage_Amazon_Proprietor_List_View.as_view()),
    path('manage_amazon_proprietor/<int:id>/', Manage_Amazon_Proprietor_Retrieve_Update_View.as_view()),
    path('amazon_proprietor_profile/', Amazon_Proprietor_Profile_View.as_view()),
]
