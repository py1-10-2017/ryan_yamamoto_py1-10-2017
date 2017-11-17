from django.shortcuts import render, HttpResponse, redirect
from .models import Course
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'course/index.html', context)

def create(request):
    errors = Course.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        Course.objects.create(
            name = request.POST['name'],
            desc = request.POST['desc'],
        )
        return redirect('/')

def remove(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, 'course/delete.html', context)

def delete(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')
