from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search', views.search, name='search'),
    path('vaccine', views.vaccine, name='vaccine'),
    path('get/ajax/country', views.ajax_search, name='ajax_search'),
    path('about', views.about, name='about'),
]