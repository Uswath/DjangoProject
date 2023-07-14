"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from cart import views
app_name ='cart'

urlpatterns = [
    path('Add_To_Cart/<int:p>', views.Add_To_Cart, name="Add_To_Cart"),
    path('cart_view',views.cart_view,name='cart_view'),
    path('decrement/<int:q>', views.decrement, name='decrement'),
    path('delete/<int:r>', views.delete, name='delete'),
    path('orderform', views.order, name='orderform'),
    path('orderview', views.orderview, name='orderview'),

]
