from .views import *
from django.urls import path

urlpatterns = [
    path("add_mobile/", Amazon_Mobile_Create_View.as_view()),
    path("mobile_list/", Amazon_Mobile_List_View.as_view())
]
