"""
URL configuration for vshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from app.views import home,about,product_list,contanct_use,supermarket,login,profile,orders,comments,favorites,ticketing_modal,checkout,categories,digital,art_culture,fashion,addresses,user,logout,rules_and_conditions
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('about/',about),
    path('product_list/',product_list),
    path('contanct_use/',contanct_use),
    path('supermarket/',supermarket),
    path('login/',login),
    path('profile/',profile),
    path('orders/',orders),
    path('comments/',comments),
    path('favorites/',favorites),
    path('ticketing_modal/',ticketing_modal),
    path('checkout/',checkout),
    path('categories/',categories),
    path('digital/',digital),
    path('art_culture/',art_culture),
    path('fashion/',fashion),
    path('addresses/',addresses),
    path('user/',user),
    path('rules_and_conditions/',rules_and_conditions),
    path('logout/',logout),
]
