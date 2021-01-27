from django.shortcuts import render

# Create your views here.
def home(req):
     return render(req, 'index.html')

def productDetail(req):
     return render(req, 'product-details.html')