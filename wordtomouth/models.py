from django.db import models
from login_app.models import User

class Recipe(models.Model):
    r_title = models.TextField()
    ingredients = models.TextField()
    preparation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    like= models.ManyToManyField(User, related_name='likes')