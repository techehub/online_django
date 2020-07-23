from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product
# Create your views here.


def myproduct_page (request):
    template = loader.get_template("productlist.html")
    data = {

        "cat" : "mobile",
        "products" : [

            {'id' :  '111',
             'name' : 'aaaa',
             'features' : ['3 mp camera', '2 gb ram']
             }
            ,
            {'id': '2222',
             'name': 'aaaa',
             'features': ['3 mp camera', '2 gb ram', '5.5 inch display', '6000 mah battery']
             }
            ,
            {'id': '3333',
             'name': 'aaaa',
             'features': ['3 mp camera', '2 gb ram']
             }
            ,
            {'id': '4444',
             'name': 'aaaa',
             'features': ['3 mp camera', '2 gb ram']
             }

        ]

    }
    res = template.render (data, request)
    return HttpResponse(res)



def product_list(request):
    template = loader.get_template("products.html")
    objects= Product.objects.all()
    data = {"products":objects}
    res = template.render(data, request)
    return HttpResponse(res)


def myproduct_detail(request, pid ):
    template = loader.get_template("product_detail.html")
    objects= Product.objects.get(id=pid)
    data = {"product":objects}
    res = template.render(data, request)
    return HttpResponse(res)

def addtocart (req):
    print (req.GET['productid'])
    print (req.GET['qty'])

    res= HttpResponse("recived")
    str= req.COOKIES.get('PID')
    if str != None :
        str= str + ","+ req.GET['productid'] + ":" + req.GET['qty']
    else :
        str = req.GET['productid'] + ":" + req.GET['qty']
    res.set_cookie("PID" , str, 24*60*60*365)
    return res

def showcart(req):
    template = loader.get_template("cart.html")

    str = req.COOKIES.get('PID')

    if str != None:
        items = str.split(',')

        cartproducts = []
        for item in items:
            vals = item.split(':')
            id = vals[0]
            qty = vals[1]
            cartproducts.append({id: qty})


        data   = { "cart" : cartproducts}
    else :
        data={}



    res = template.render(data, req)
    return HttpResponse(res)
