from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('user/<int:poster_id>', views.user_recipes),
    path('myaccount/<int:recipe_id>', views.edit),
    path('<int:recipe_id>/update', views.update)
]