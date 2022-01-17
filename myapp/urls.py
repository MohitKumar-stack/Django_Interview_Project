from django.contrib import admin
from django.urls import path,include
from myapp import views
urlpatterns = [
    path("",views.index,name='login'),
    path("login/",views.index,name='login'),
    path("Signup/",views.Signup,name='Signup'),
    path("home/",views.Home,name='Home'),
    path("delete/<str:id>",views.delete,name='delete'),
    path("edit/<str:id>",views.edit,name='edit'),
    path("update/<str:id>",views.update,name='update')


]
