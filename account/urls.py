from django.urls import path

from . import views

urlpatterns = [
    path('loginPage', views.loginPage, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logoutUser, name='logout'),
]