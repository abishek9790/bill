from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def materials(request):
    mf=materialform()
    d={'mf':mf}
    if request.method=='POST':
        data=materialform(request.POST)
        if data.is_valid():
            mfo=data.save(commit=False)
            mfo.save()
            messages.success(request,'Registration done thank you')
        else:
            messages.error(request, 'Registration failed')
    return render(request, 'materials.html',d)

def party_form(request):
    pf=partyform()
    d={'pf':pf}
    if request.method=='POST':
        dat=partyform(request.POST)
        if dat.is_valid():
            mf=dat.save(commit=False)
            mf.save()
            messages.success(request,'Registration done thank you')
        else:
            messages.error(request, 'Registration failed')
    return render(request, 'party_form.html',d)

def hsnform(request):
    pfa=hsn_form()
    d={'pfa':pfa}
    if request.method=='POST':
        da=hsn_form(request.POST)
        if da.is_valid():
            mfo=da.save(commit=False)
            mfo.save()
            messages.success(request,'Registration done thank you')
        else:
            messages.error(request, 'Registration failed')
    return render(request, 'hsnform.html',d)

def invoiceform(request):
    ifo=invoice_form()
    d={'ifo':ifo}
    if request.method=='POST':
        do=invoice_form(request.POST)
        if do.is_valid():
            mfa=do.save(commit=False)
            mfa.save()
    return render(request, 'invoiceform.html',d)
