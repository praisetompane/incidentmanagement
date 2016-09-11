from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'manager/home.html') #can pass a dictionary as well
