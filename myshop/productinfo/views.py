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
    return HttpResponse("recived")