from .views import *
from django.urls import path, include

urlpatterns = [
    path('amazon_employee_signup/', Amazon_Employee_Signup_View.as_view()),
    path('amazon_employee_notification/', Amazon_Employee_Notifications_View.as_view()),
    path('amazon_employee_list/', Amazon_Employee_ListView.as_view()),
]
