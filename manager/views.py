#!python
# log/views.py
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from manager.forms import *
from manager.models import *
from manager.viewutilities import *


# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
    # Get all maintenance requests for a user
    user = request.user
    requests = MaintananceRequest.objects.all().filter(userid=user.id)[5:10]
    return render(request, "main.html", {'user': user,
                                         'requests': requests})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        profileForm = ProfileForm(request.POST)
        if userForm.is_valid() & profileForm.is_valid():
            newUser = User.objects.create_user(username=userForm.cleaned_data['username'],
                                               password=userForm.cleaned_data['password'],
                                               email=userForm.cleaned_data['email'])
            newUser.save()
            profileForm = ProfileForm(request.POST, instance=newUser.profile)
            userProfile = profileForm.save(commit=False)
            userProfile.save()
        else:
            return render(request, 'registration/register.html', {'userForm': userForm, 'profileForm': ProfileForm})
        return HttpResponseRedirect('/login')

    else:
        userForm = UserForm()
        profileForm = ProfileForm()
        return render(request, 'registration/register.html', {'userForm': userForm, 'profileForm': ProfileForm})


def updateUser(request):
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        profileForm = ProfileForm(request.POST)
        if userForm.is_valid() & profileForm.is_valid():
            UserForm.save()
            profileForm.save()
        else:
            return render(request, 'registration/register.html', {'userForm': userForm, 'profileForm': ProfileForm})

    else:
        user = get_object_or_404(User, pk=request.user.id)  # if post, then update
        profile = Profile.objects.get(user=user)
        userForm = UserForm(user)
        profileForm = ProfileForm(profile)
        return render(request, 'registration/register.html', {'userForm': userForm, 'profileForm': ProfileForm})


# else get the user's details and default the forms

def register_success(request):
    return render(request, 'registration/success.html')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url="login/")
@csrf_exempt
def createMaintenanceRequest(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            referenceNo = generateReferenceNumber()
            interimForm = form.save(commit=False)
            interimForm.referenceNumber = referenceNo
            interimForm.userid_id = user.id
            userprofileresid = User.objects.get(id=user.id)
            interimForm.save()

            # Need to get the user associated with this maintainer
            # Link maintainer to User??

            '''
            residenceMaintainers = ResidenceMaintainer.objects.all().filter(residence=interimForm.residence)
                        users = User.objects.all()

                        for resMan in residenceMaintainers:
                            residenceMaintainerUser = User.objects.all().filter(id=resMan.maintainer)
            '''

            sendAcknowledgementEmail(interimForm.type, referenceNo, [user.email])
            # completedrequests = MaintananceRequest.objects.all().filter(userid=user.id)
            return render(request, 'maintenance/successcreate.html', {'form': interimForm, 'user': user})
    else:
        user = request.user
        userRequests = MaintananceRequest.objects.all().filter(userid=user.id)
        form = MaintenanceForm()
    return render(request, 'maintenance/maintenance.html', {'form': form,
                                                            'requests': userRequests})


def dashboard(request):
    return render(request, 'dashboard.html')


def updateMaintenanceRequest(request, pk):
    if request.method == 'POST':
        maintenanceRequest = get_object_or_404(MaintananceRequest, pk=pk)
        form = MaintenanceForm(request.POST, request.FILES, instance=maintenanceRequest)
        if form.is_valid():
            form.save()
            return render(request, 'maintenance/successupdate.html')
    else:
        user = request.user
        userRequests = MaintananceRequest.objects.all().filter(userid=user.id)
        maintenanceRequest = get_object_or_404(MaintananceRequest, pk=pk)
        form = MaintenanceForm(request.POST, request.FILES, instance=maintenanceRequest)

    return render(request, 'maintenance/requestdetail.html', {'form': form,
                                                              'requests': userRequests})
