from django.urls import path
from . import views

urlpatterns =  [
    path(route='index', view=views.index, name='index'),
    path(route='animechan', view=views.animechan, name='animechan'),
]

