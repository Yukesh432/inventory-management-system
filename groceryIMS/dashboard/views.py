from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')

def staff(request):
    return render(request, 'dashboard/staff.html')

def allproducts(request):
    return render(request, 'partials/products.html')

def expiredproducts(request):
    return render(request, 'partials/expired.html')