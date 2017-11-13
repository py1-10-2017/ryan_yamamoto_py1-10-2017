from django.shortcuts import render, HttpResponse, redirect
import datetime

# Create your views here.
def index(request):
    return render(request, "session_words/index.html")

def process(request):
    if 'the_list' not in request.session:
        request.session['the_list'] = []
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1

    if 'font_size' in request.POST:
        big_font = True
    else:
        big_font = False
    new_word_dict = {
        "word": request.POST['word'],
        "color": request.POST['color'],
        "big_font": big_font,
        "time": datetime.datetime.now().strftime("%B, %d at %H:%m:%p")
    }

    request.session['the_list'].append(new_word_dict)
    return redirect('/')

def reset(request):
    try:
        del request.session['the_list']
        del request.session['count']
    except:
        pass #if no try and except this will cause a keyerror when clearing without info in box
    return redirect('/')
