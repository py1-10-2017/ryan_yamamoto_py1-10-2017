from __future__ import unicode_literals
import bcrypt
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserManager(models.Manager):
    def validate(self, post_data):
        errors = [] # populate list of strings that returns back to views.py
        # first_name 2 or more
        if len(post_data['first_name']) < 2:
            errors.append("First name must be more than 2 characters")
        # last_name 2 or more
        if len(post_data['last_name']) < 2:
            errors.append("Last name must be more than 2 characters")
        # email valid format
        if not re.match(EMAIL_REGEX, post_data['email']):
                errors.append("Email address invalid")
        else:
            # email exits already
            if self.filter(email=post_data['email']):
                errors.append("Email exists already")
        # password 8 or more
        if len(post_data['password']) < 8:
            errors.append("Password must be more than 8 characters")
        # confirm password
        if post_data['password'] != post_data['confirm_password']:
            errors.append("Confirm password must match Password")
        return errors #funtion will return a list

    def create_user(self, clean_data):
        hashed = bcrypt.hashpw(clean_data['password'].encode(), bcrypt.gensalt())
        return self.create(
            first_name = clean_data['first_name'],
            last_name = clean_data['last_name'],
            email = clean_data['email'],
            password = hashed
        )

    def validate_login(self, post_data):
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
        return (errors, the_user)




        # if not errors:
        #     hashed = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
        #     self.create(
        #         first_name = post_data['first_name'],
        #         last_name = post_data['last_name'],
        #         email = post_data['email'],
        #         password = hashed
        #     )



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    def __str__(self):
        return self.email
