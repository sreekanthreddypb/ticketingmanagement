from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.home , name="home"),
    path('customers/<str:pk_test>/', views.customers, name="customer"),
    path('tickets/', views.tickets, name="tickets"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('create_ticket/<str:pk>', views.createTicket, name="create_ticket"),
    path('user/', views.userPage, name="user-page"),
    path('update_ticket/<str:pk>/', views.updateTicket, name="update_ticket"),
    path('delete_ticket/<str:pk>/', views.deleteTicket, name="delete_ticket"),
]