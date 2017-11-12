from django.shortcuts import render, HttpResponse, redirect
import random, datetime
# Create your views here.


def index(request):
    try:
        request.session['mygold']
    except KeyError:
        request.session['mygold'] = 0
    return render(request, 'ninja_gold/index.html')

def process(request):
    try:
        temp = request.session['activity']
    except KeyError:
        temp = []

    if request.POST['building'] == 'farm':
        result = random.randrange(10,21)

    elif request.POST['building'] == 'cave':
        result = random.randrange(5,11)

    elif request.POST['building'] == 'house':
        result = random.randrange(2,6)

    elif request.POST['building'] == 'casino':
        result = random.randrange(-50,51)

    message = "You earned/lost {} at {}".format(result, datetime.datetime.now().strftime("%B, %d at %H:%m:%p"))
    request.session['mygold'] = int(request.session['mygold']) + result
    temp.append(message)
    request.session['activity'] = temp
    return redirect('/')

def reset(request):
    del request.session['mygold']
    del request.session['activity']
    return redirect('/')
