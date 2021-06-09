from django.shortcuts import render
#from Jobs.models import *
from accounts.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordResetForm

# Create your views here.

def index(request):
    context={
       # 'jobs':Jobs.objects.all(),
        #'job_category':Category.objects.all(),
        'formsignin':AuthenticationForm(),
        'password_reset':PasswordResetForm(),
        'formsigup':SignupForm(),
        'resetform':PasswordResetForm(),
        #'profileform': ProfileForm(),
        
    }
    return render(request, 'pages/index.html',context)


def about(request):
    return render(request, 'pages/about.html',{"form_login":AuthenticationForm()})