from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.http import HttpResponse, JsonResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def topics(request):
    return render(request, 'my-topics.html')

def knowledge_center(request):
    return render(request, 'knowledge-center.html')

def CONPI_certificate(request):
    return render(request, 'CONPI-certificate.html')

def enquiries_faq(request):
    return render(request, 'enquiries-faq.html')

def CONPI_Application_Form(request):
    form = conpi_forms()

    if request.method == 'POST':
        form = conpi_forms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Application saved successfully')
            return redirect('CONPI_Application_Form')
    context = {
        'form':form,
    }
    return render(request, 'CONPI-Application-Form.html', context)


def get_conpi(request):
     obj_models = list(conpi.objects.values())
     return JsonResponse({'data':obj_models})
   