from django.urls import path
from . import views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('create', views.create, name='create'),
    path('profile',views.profile,name='profile'),
]
