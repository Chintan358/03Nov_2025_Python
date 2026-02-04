from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def reg(request):
    data = request.GET['data']
    return HttpResponse(f" Hello , {data}")
    
def search(request):
    q = request.GET['q']
    # resp = ""
    # if q == "electric":
    #     resp+="<ul><li>Fan</li><li>TV</li><li>Mobile</li></ul>"
    # elif q == "sports":
    #     resp+="<ul><li>Bat</li><li>Ball</li><li>Hockey</li></ul>"
    # elif q == "cloths":
    #     resp+="<ul><li>Shirt</li><li>T-shirt</li><li>Cap</li></ul>"
    # else:
    #     resp+="No data found"


    products = Product.objects.filter(name__startswith=q)
    resp = "<ul>"
    for product in products:
        resp+=f"<li>{product.name}</li>"
    resp+="</ul>"
    return HttpResponse(resp)

def countries(request):
    clist = Country.objects.all()
    return JsonResponse({"clist":list(clist.values())})

def states(request):
    cid = request.GET['cid']
    slist = State.objects.filter(country_id=cid)
    return JsonResponse({"slist":list(slist.values())})