from django.contrib import admin
from django.urls import path, include
from .views import contact, contact_save


urlpatterns = [ path ('get', contact),
                path ('save', contact_save)]