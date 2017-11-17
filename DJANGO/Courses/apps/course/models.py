from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['name']) < 5:
            errors.append("Name must be 5 or more chararters")
        if len(post_data['desc']) < 15:
            errors.append("Description must be 15 or more chararters")
        return errors
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
    def __str__(self):
        return self.name
