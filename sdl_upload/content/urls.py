from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('user/', views.userPage, name='user-page'),

    path('accounts/', views.accountSettings, name='account'),

    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]
