from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'login_reg/index.html')

def register(request):
    errors = User.objects.validate(request.POST) #lets me use post_data in UserManager
    if errors:
        for e in errors:
            messages.error(request, e)
    else:
        # make a user
        new_user = User.objects.create_user(request.POST)
        request.session['id'] = new_user.id
        messages.success(request, "Thank you {} for registering".format(new_user.first_name))
    return redirect('/')

def success(request):
    return render(request, 'login_reg/success.html')

def login(request):
    result = User.objects.validate_login(request.POST)
    if result[0]:
        for e in result[0]:
            messages.error(request, e)
            return redirect('/')
    else:
        request.session['id'] = result[1].id
        request.session['first_name'] = result[1].first_name
        return redirect('/success')

def logout(request):
    del request.session['id']
    del request.session['first_name']
    return redirect('/')
