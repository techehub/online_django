from django.shortcuts import render
from django.template import loader
# Create your views here.

from .models import Contact

from django.http import HttpResponse

def contact (req):
    template = loader.get_template("contact.html")
    data = {}
    res = template.render(data, req)
    return HttpResponse(res)

def contact_save(req):
    print (req.POST)
    print(req.POST['name'])
    print(req.POST['email'])
    print(req.POST['phone'])

    c = Contact(name= req.POST['name'], email=req.POST['email'], phone=req.POST['phone'])
    c.save ()
    return HttpResponse("Get data !!!")


