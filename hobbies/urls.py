import imp
from django.urls import path
from . import views
import hobbies

app_name = "hobbies"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]