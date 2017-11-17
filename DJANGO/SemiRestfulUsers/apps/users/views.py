from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, 'users/index.html', context)

def new(request):
    return render(request, 'users/new.html')

def create(request):
    errors = User.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('/new')
    else:
        User.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            password = request.POST['password']
        )
        return redirect('/')

def show(request, user_id):
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request, 'users/show.html', context)

def edit(request, user_id):
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request, 'users/edit.html', context)

def update(request, user_id):
    user = User.objects.get(id=user_id)
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.save()
    return redirect('/')

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/')
