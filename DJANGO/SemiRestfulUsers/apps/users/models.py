from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['name']) < 3:
            errors.append("Name must be 3 or more chararters")
        if len(post_data['password']) < 5:
            errors.append("Password must be 5 or more chararters")
        return errors
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.name
