"""
URL configuration for hotels project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view
from mainApp.views import main_page_view, redirect_to_main, reserve_hotel_view, register, payment_view, profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_main, name="redirect-main"),
    path('register/', register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('hotels-main/', main_page_view, name='hotels-main'),
    path('reserve-hotel/', reserve_hotel_view, name='reserve-hotel'),
    path('payment-page/', payment_view, name='payment-page'),
    path('profile/', profile_view, name='profile')
]