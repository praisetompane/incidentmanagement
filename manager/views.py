#!python
# log/views.py
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt

from manager.forms import *


# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")


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
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            user = request.user
            referenceNo = generateReferenceNumber()
            maintenanceRequest = form.save(commit=False)
            maintenanceRequest.referenceNumber = referenceNo
            maintenanceRequest.save()
            '''
                 send_mail(
                'Maintenance Request',
                'Thank you for logging you request, your reference number is:' + referenceNo,
                'ssms@example.com',
                [user.email],
                fail_silently=False,
            )
            '''

            return render(request, 'maintenance/success.html', {'form': maintenanceRequest})
    else:
        form = MaintenanceForm()

    # sending an email in Django: https://docs.djangoproject.com/en/1.10/topics/email/
    '''
        request.FILES
        https://docs.djangoproject.com/en/1.10/ref/forms/api/#binding-uploaded-files
    '''
    return render(request, 'maintenance/maintenance.html', {'form': form})


def existingMaintenanceRequests(request):
    # after creating a new maintenace request, refresh the Track Existing Maintenance
    # maintenacerequests.objects.all(where useris= request.userid)
    render(request, 'maintenance/existingmaintenance.html')


def generateReferenceNumber():
    return get_random_string(length=10)
