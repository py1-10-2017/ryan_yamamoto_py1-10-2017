from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
items = [
    {
        'item': 'Dojo Tshirt',
        'price': 19.99,
        'id': 1
    },
    {
        'item': 'Dojo Sweater',
        'price': 29.99,
        'id': 2
    },
    {
        'item': 'Dojo Cup',
        'price': 4.99,
        'id': 3
    },
    {
        'item': 'Algorithm Book',
        'price': 49.99,
        'id': 4
    },
]
def index(request):
    if "last_transaction" in request.session.keys():
        del request.session['last_transaction']
    context = {
        'items': items
    }
    return render(request, 'amadon_store/index.html', context)

def buy(request, item_id):
    for item in items:
        if item['id'] == int(item_id):
            amount_charged = item['price'] * int(request.POST['quantity'])

    try:
        request.session['total_charged']
    except KeyError:
        request.session['total_charged'] = 0

    try:
        request.session['total_items']
    except KeyError:
        request.session['total_items'] = 0

    request.session['last_transaction'] = amount_charged
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['total_charged'] += amount_charged

    # return redirect('/checkout')

    # if request.POST['item'] == 1:
    #     price = 19.99
    # if request.POST['item'] == 2:
    #     price = 29.99
    # if request.POST['item'] == 3:
    #     price = 4.99
    # if request.POST['item'] == 4:
    #     price = 49.99
    # else:
    #     price = 0

    # if request.POST['product_id'] == '1':
    #     price = 19.99
    # elif request.POST['product_id'] == '2':
    #     price = 29.99
    # elif request.POST['product_id'] == '3':
    #     price = 4.99
    # elif request.POST['product_id'] == '4':
    #     price = 49.99
    # else:
    #     price = 0
    # total = int(request.POST['quantity']) * price
    # try:
    #     request.session['items'] += int(request.POST['quantity'])
    #     request.session['last_charge'] = total
    #     request.session['total_spent'] += total
    # except: # will error if items cleared and started over
    #     request.session['items'] = int(request.POST['quantity'])
    #     request.session['last_charge'] = total
    #     request.session['total_spent'] = total
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'amadon_store/checkout.html')

def reset(request):
    for sesh in request.session.keys():
        del request.session[sesh]
    return redirect('/')
