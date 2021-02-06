from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('success',views.success),
    path('logout',views.logout),
    path('login',views.login),
    path('users/<userid>',views.info),
    path('delete/<quoteid>',views.delete),
    path('add/<quoteid>',views.like),
    path('edit/<quoteid>',views.edit),
    path('remove/<quoteid>',views.unlike),
    path('update/<quoteid>',views.update),
    path('create',views.create),
]