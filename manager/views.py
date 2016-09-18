#!python
# log/views.py
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from manager.forms import *
from manager.models import MaintananceRequest


# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {
            'form': form
        })

    return render_to_response(
        'registration/register.html',
        variables,
    )

def register_success(request):
    return render_to_response(
        'registration/success.html',
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url="login/")
@csrf_exempt
def maintenance(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
           #Do some DB work here
    else:
        form = MaintenanceForm()

    return render(request, 'maintenance/maintenance.html', {'form': form})


def existingMaintenanceRequests(request):
    #after creating a new maintenace request, refresh the Track Existing Maintenance
    #maintenacerequests.objects.all(where useris= request.userid)
    render(request,'maintenance/existingmaintenance.html')



