from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    try:
        request.session['times'] += 1
    except:
        request.session['times'] = 0
    return render(request, 'random_word/index.html')

def generate(request):
    request.session['word'] = get_random_string(14)
    return redirect('/')

def reset(request):
    for sesh in request.session.keys():
        del request.session[sesh]
    return redirect('/')
