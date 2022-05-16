from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('stockDetails', views.stockDetails, name='stockDetails'),
    path('ticker', views.ticker, name='ticker'),
]
