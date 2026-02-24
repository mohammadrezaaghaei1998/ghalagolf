from django.urls import path
from . import views

urlpatterns = [
    path('member-lounge', views.member_lounge, name='member-lounge'),
]

