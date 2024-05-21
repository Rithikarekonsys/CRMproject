from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name='create'),
    path('profile',views.profile,name='profile'),
    path('signin',views.signin,name='signin'),
]
