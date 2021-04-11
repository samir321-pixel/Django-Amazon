from .views import *
from django.urls import path, include

urlpatterns = [
    path('amazon_admin_signup/', Amazon_Admin_Signup_View.as_view()),
    path('amazon_admin_notification/', Amazon_Admin_Notification_View.as_view()),
    path('amazon_admin_list/', Manage_Amazon_Admin_ListView.as_view()),
    path('amazon_admin_list/<int:id>/', Manage_Amazon_Admin_Retrieve_View.as_view()),
    path('amazon_admin_profile/', Amazon_Admin_Profile_View.as_view()),

]
