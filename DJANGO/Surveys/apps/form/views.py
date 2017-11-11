from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'form/index.html')



def process(request):
    if "count" in request.session:
        request.session["count"] += 1
    else:
        request.session["count"] = 0
    request.session["name"] = request.POST["name"]
    request.session["location"] = request.POST["location"]
    request.session["language"] = request.POST["language"]
    request.session["comment"] = request.POST["comment"]
    return redirect('/results')

def results(request):
    return render(request, 'form/results.html')
