from django.urls import path

from . import views

urlpatterns = [
    path('set', views.favourite, name='map'),
    path('like', views.like, name='map')
]