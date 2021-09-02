from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
#from django.conf import 
# Create your views here.
def index(request):
    return render(request,'index.html')

def destinations(request):
    return render(request,'destination.html')