from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import mRegister
from .forms import *
from django.utils import timezone


# Create your views here.

def LandingPage(request):
    return render(request, 'landingPage.html')


def Register(request):
    if request.method =='POST':
        form = regForm(request.POST)
        if form.is_valid():
            reg = mRegister()
            reg.Aadhar = form.cleaned_data["Aadhar"]
            reg.Name = form.cleaned_data["Name"]
            reg.Dob = form.cleaned_data["Dob"]
            reg.Phone = form.cleaned_data["Phone"]
            reg.PinCode = form.cleaned_data["PinCode"]
            reg.VDate = form.cleaned_data["VDate"]
            reg.VSlot = form.cleaned_data["VSlot"]
            reg.save()
    else:
        form =regForm()

    return render(request, 'Register.html', locals())



def Registrations(request):
    all_regs = mRegister.objects.all()

    context = {
        'all_regs': all_regs
    }

    return render(request, 'Display.html', context)

def Aboutus(request):
    return render(request, 'contact.html')
