from django.urls import path
from . import views

urlpatterns = [
    path('recipes', views.dashboard),
    path('recipe/create', views.create_recipe),
    path('<int:recipe_id>/delete', views.delete_recipe),
]