from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mylist/', views.mylist, name='mylist'),
]