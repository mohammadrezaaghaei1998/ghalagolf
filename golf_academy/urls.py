from django.urls import path
from . import views

urlpatterns = [
    
    path('golf-academy', views.golf_academy, name='golf-academy'),
]

