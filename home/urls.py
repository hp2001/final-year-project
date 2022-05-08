from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('stockDetails', views.stockDetails, name='stockDetails'),
    # path('login', views.login, name='login'),
    # path('register', views.register, name='register'),
    path('tcs', views.tcs, name='tcs'),
    path('fis', views.fis, name='fis'),
    path('epam', views.epam, name='epam'),
    path('amazon', views.amazon, name='amazon'),
    path('capgemini', views.capgemini, name='capgemini'),
]
