from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def register(request):
    response = "display 'placeholder for users to create a new user record"
    return HttpResponse(response)

def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)

def new(request):
    response = "placeholder for users to add a new survey NEW"
    return HttpResponse(response)

def users(request):
    response = "placeholder for users to add a new survey USERS"
    return HttpResponse(response)
