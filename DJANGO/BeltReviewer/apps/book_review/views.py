from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'book_review/index.html')

def register(request):
    errors_or_users = User.objects.validate(request.POST)
    # result = User.objects.validate(request.POST) #lets me use post_data in UserManager
    # if type(result) == list:
    if errors_or_users[0]:
        for e in errors_or_users[0]:
            messages.error(request, e)
        return redirect('/')
    else:
        # make a user
        # new_user = User.objects.validate(request.POST)
        request.session['user_id'] = errors_or_users[1].id
    return redirect('/home')

def home(request):
    if not 'user_id' in request.session.keys():
        print "no user here"
        return redirect('/') #return a key error if went to /success page and not logged in
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "three": Review.objects.recent()[0],
        "notthree": Review.objects.recent()[1]
    }
    return render(request, 'book_review/home.html', context)

def login(request):
    result = User.objects.validate_login(request.POST)
    if result[0]: # list of errors [0]
        for e in result[0]:
            messages.error(request, e)
            return redirect('/')
    else:
        request.session['user_id'] = result[1].id # setting session id to user from tuple [1]
        return redirect('/home')

def logout(request):
    for sesh in request.session.keys():
        del request.session[sesh]
    return redirect('/')

def add_book(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'book_review/newbook.html', context)

def show_book(request, book_id):
    context = {
        "book": Book.objects.get(id=book_id),
    }

    return render(request, 'book_review/show_book.html', context)

def post_book(request):
    errs = Review.objects.validate_review(request.POST)
    if errs:
        for e in errs:
            messages.error(request, e)
        return redirect('/add_book')
    else:
        book_id = Review.objects.create_review(request.POST, request.session['user_id']).book.id
    print "GOOD"
    return redirect('/book/{}'.format(book_id))

def create(request, book_id):
    this_book = Book.objects.get(id=book_id)
    new_review = {
        "title": this_book.title,
        "author": this_book.author.name,
        "review": request.POST['review'],
        "rating": request.POST['rating']
    }
    errs = Review.objects.messages_new(new_review) #made query for practice
    if errs:
        for e in errs:
            messages.error(request, e)
    else:
        Review.objects.create_new(new_review, request.session['user_id']) #made query for practice
    return redirect('/book/{}'.format(book_id))

    # this_book = Book.objects.get(id=book_id)
    # new_review = {
    #     "title": this_book.title,
    #     "author": this_book.author.name,
    #     "review": request.POST['review'],
    #     "rating": request.POST['rating'],
    #     "new_author": ''
    # }
    # errs = Review.objects.validate_review(new_review)
    # if errs:
    #     for e in errs:
    #         messages.error(request, e)
    # else:
    #     Review.objects.create_review(new_review, request.session['user_id'])
    # return redirect('/book/{}'.format(book_id))

def show_user(request, user_id):
    context = {
        'user': User.objects.get(id=user_id),
        'reviews': Review.objects.filter(user_id=user_id),
        'total_reviews': len(Review.objects.filter(user_id=user_id))
    }
    return render(request, 'book_review/show_user.html', context)

def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    book_id = Review.objects.get(id=review_id).book.id
    if review.user.id == request.session['user_id']:
        review.delete()
    return redirect('/book/{}'.format(book_id))
