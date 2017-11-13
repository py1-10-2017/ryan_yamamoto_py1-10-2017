from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'amadon_store/index.html')

def buy(request):
    if request.POST['product_id'] == '1':
        price = 19.99
    elif request.POST['product_id'] == '2':
        price = 29.99
    elif request.POST['product_id'] == '3':
        price = 4.99
    elif request.POST['product_id'] == '4':
        price = 49.99
    else:
        price = 0
    total = int(request.POST['quantity']) * price
    try:
        request.session['items'] += int(request.POST['quantity'])
        request.session['last_charge'] = total
        request.session['total_spent'] += total
    except: # will error if items cleared and started over
        request.session['items'] = int(request.POST['quantity'])
        request.session['last_charge'] = total
        request.session['total_spent'] = total
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'amadon_store/checkout.html')

# def reset(request):
#     del request.session['last_charge']
#     del request.session['total_spent']
#     del request.session['items']
#     return redirect('/')
