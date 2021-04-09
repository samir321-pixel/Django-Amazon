from .views import *
from django.urls import path, include

urlpatterns = [
    path('amazon_employee_signup/', Amazon_Employee_Signup_View.as_view()),
]
