from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
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

def myproduct_detail(request):
    return HttpResponse("This is my product detail page")