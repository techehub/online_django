
from django.urls import path
from .views import myproduct_page, myproduct_detail
urlpatterns = [

    path ('info', myproduct_page),
    path ('detail', myproduct_detail)
]
