""" Urls and the link to the code for this url (views.<name>) """
from django.urls import path

from . import views
app_name = "myportfolio"

urlpatterns = [
    path("", views.index, name="index"),
    path("resume", views.resume, name="resume")
]
