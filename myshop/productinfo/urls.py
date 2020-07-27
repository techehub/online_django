
from django.urls import path
from .views import myproduct_page, myproduct_detail, product_list, addtocart, showcart, getProducts, search, getdata
urlpatterns = [

    path ('info', myproduct_page),
    path ('detail/<str:pid>', myproduct_detail),
    path ('products' , product_list),
    path ('addtocart', addtocart),
    path ('showcart', showcart),
    path ('getall/<str:key>', getProducts),
    path ('productsearch', search),
    path('data', getdata),

]
