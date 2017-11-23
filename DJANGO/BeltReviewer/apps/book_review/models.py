from __future__ import unicode_literals
import bcrypt
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserManager(models.Manager):
    def validate(self, post_data):
        errors = [] # populate list of strings that returns back to views.py
        the_user = None
        # first_name 2 or more
        if len(post_data['name']) < 2:
            errors.append("Name must be more than 2 characters")
        # last_name 2 or more
        if len(post_data['alias']) < 2:
            errors.append("Alias must be more than 2 characters")
        # email valid format
        if not re.match(EMAIL_REGEX, post_data['email']):
                errors.append("Email address invalid")
        else:
            # email exits already
            if self.filter(email=post_data['email']):
                errors.append("Email exists already")
        # password 4 or more
        if len(post_data['password']) < 4:
            errors.append("Password must be more than 4 characters")
        # confirm password
        if post_data['password'] != post_data['confirm_password']:
            errors.append("Confirm password must match Password")
        # return errors #funtion will return a list

        if not errors:
            hashed = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
            the_user = self.create(
                name = post_data['name'],
                alias = post_data['alias'],
                email = post_data['email'],
                password = hashed
            )
        return (errors, the_user)
    # def create_user(self, clean_data):
    #     hashed = bcrypt.hashpw(clean_data['password'].encode(), bcrypt.gensalt())
    #     return self.create(
    #         name = clean_data['name'],
    #         alias = clean_data['alias'],
    #         email = clean_data['email'],
    #         password = hashed
    #     )

    def validate_login(self, post_data):
        """
        check post request for valid data
        if valid, returns tuple ([], <User Object>)
        if not, returns ([error list], None)
        """
        errors = []
        the_user = None
        #email is not in system
        if not self.filter(email=post_data['email']):
            errors.append("Incorrect email/password")
        else:
            the_user = self.get(email=post_data['email'])
            #password is incorrect
            if not bcrypt.checkpw(post_data['password'].encode(), the_user.password.encode()):
                errors.append("Incorrect email/password")
                the_user = None
        return (errors, the_user) #tuple of errors and users ([errors], <user>)


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class ReviewManager(models.Manager):
    def validate_review(self, post_data):
        errors = []
        if len(post_data['title']) < 1 or len(post_data['review']) < 1:
            errors.append("Fields are required")
        if not "author" in post_data and len(post_data['new_author']) < 3:
            errors.append("New author names must be 3 or more characters")
        if "author" in post_data and len(post_data['new_author']) > 0 and len(post_data['new_author']) < 3:
            errors.append("New author names must be 3 or more characters")
        # if not int(post_data['rating']) > 0 or not int(post_data['rating']) <= 5:
        #     errors.append('invalid rating')
        return errors

    def create_review(self, clean_data, user_id):
        the_author = None
        if len(clean_data['new_author']) < 1:
            try:
                the_author = Author.objects.get(id=int(clean_data['author']))
            except:
                the_author = Author.objects.get(name=clean_data['author'])
        else:
            the_author = Author.objects.create(name=clean_data['new_author'])

        the_book = None
        if not Book.objects.filter(title=clean_data['title']):
            the_book = Book.objects.create(
                title = clean_data['title'],
                author = the_author
            )
        else:
            the_book = Book.objects.get(title=clean_data['title'])
        return self.create(
            review = clean_data['review'],
            rating = clean_data['rating'],
            book = the_book,
            user = User.objects.get(id=user_id)
        )

    def messages_new(self, post_data):
        errors = []
        if len(post_data['review']) < 1:
            errors.append("cannot leave blank")
        return errors

    def create_new(self, post_data, user_id):
        the_book = Book.objects.get(title=post_data['title'])
        the_author = Author.objects.get(name=post_data['author'])
        return self.create(
            review = post_data['review'],
            rating = post_data['rating'],
            user = User.objects.get(id=user_id),
            book = the_book
        )

    def recent(self):
        return (self.all().order_by('-created_at')[:3], self.all().order_by('-created_at')[3:])


class Review(models.Model):
    review = models.TextField(max_length=1000)
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ReviewManager()
    def __str__(self):
        return "Book: {}".format(self.book.title)
