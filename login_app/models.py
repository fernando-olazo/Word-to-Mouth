from django.db import models
import re
import bcrypt

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, input_stuff):
        errors = {}
        if len(input_stuff['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if len(input_stuff['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        if len(input_stuff['email']) == 0:
            errors['email'] = "Please enter an email"
        elif not email_regex.match(input_stuff['email']):
            errors['email'] = "Please enter a valid email address"
        valid_user = User.objects.filter(email=input_stuff['email'])
        if len(valid_user) > 0:
            errors['email_inuse'] = "The email address you have entered is already in use"
        if len(input_stuff['password']) < 6:
            errors['password'] = "Password must be at least 6 characters long"
        if input_stuff['password'] != input_stuff['confirm_password']:
            errors['mismatch'] = "Your passwords do not match"
        return errors
    
    def login_validator(self, input_stuff):
        errors = {}
        current_user = User.objects.filter(email=input_stuff['email'])
        if len(input_stuff['email']) == 0:
            errors['email'] = "Email is required"
        if len(input_stuff['password']) < 6:
            errors['password'] = "Your password must be at least 6 characters"
        elif bcrypt.checkpw(input_stuff['password'].encode(), current_user[0].password.encode()) != True:
            errors['password'] = "Your Password or Email is incorrect"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()