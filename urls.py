from turtle import home
from django.urls import path
from . import views
app_name = "template"

urlpatterns = [
    path("",views.home,name="test")
]