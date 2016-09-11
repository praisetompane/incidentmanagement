from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'manager/home.html') #can pass a dictionary as well

#Change this to an actual contact us page
def contact(request):
    return render(request, 'manager/basic.html', {'content':['If you would like to contact us, please use our email:','x@incidentmanagement.com']})
