from .views import *
from django.urls import path, include

urlpatterns = [
    path('amazon_admin_signup', Amazon_Admin_Signup_View.as_view()),
]
