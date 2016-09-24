#!python
# log/views.py
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt

from manager.forms import *
from manager.models import *


# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
    # Get all maintenance requests for a user
    user = request.user
    completedrequests = MaintananceRequest.objects.all().filter(userid=user.id)

    # outstandingrequests = MaintananceRequest.objects.all().filter(userid=user.id).filter(status!='Complete')

    return render(request, "home.html", {'outstandingrequests': completedrequests,
                                         'completedrequests': completedrequests})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            newUser = User.objects.create_user(
                username=userForm.cleaned_data['username'],
                password=userForm.cleaned_data['password'],
                email=userForm.cleaned_data['email']
            )
            newUser.save()
            profileForm = ProfileForm(request.POST, instance=newUser.profile)
            if profileForm.is_valid():
                userProfile = profileForm.save(commit=False)
                userProfile.save()
            return HttpResponseRedirect('/register/success/')
    else:
        userForm = UserForm()
        profileForm = ProfileForm()
    return render(request, 'registration/register.html', {'userForm': userForm, 'profileForm': ProfileForm})


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
        form = MaintenanceForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            referenceNo = generateReferenceNumber()
            interimForm = form.save(commit=False)
            interimForm.referenceNumber = referenceNo
            interimForm.userid_id = user.id
            interimForm.save()
            send_mail(
                'Maintenance Request for' + interimForm.type,
                'Thank you for logging you request, your reference number is:' + referenceNo,
                'simplemaintenances@gmail.com',
                [user.email],
                fail_silently=False)

            return render(request, 'maintenance/successcreate.html', {'form': interimForm, 'user': user})
    else:
        form = MaintenanceForm()
    return render(request, 'maintenance/maintenance.html', {'form': form})


def generateReferenceNumber():
    return get_random_string(length=10)


def updateMaintenance(request, pk):
    if request.method == 'POST':
        maintenanceRequest = get_object_or_404(MaintananceRequest, pk=pk)
        form = MaintenanceForm(request.POST, request.FILES, instance=maintenanceRequest)
        if form.is_valid():
            form.save()
            return render(request, 'maintenance/successupdate.html')
    else:
        maintenanceRequest = get_object_or_404(MaintananceRequest, pk=pk)
        form = MaintenanceForm(request.POST, request.FILES, instance=maintenanceRequest)

    return render(request, 'maintenance/requestdetail.html', {'form': form})
