"""execpenal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from execapi import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #Config rest_framework
    path('auth/', include('rest_framework.urls')),
    #Api
    path('api/v1/', include('execapi.urls'))
]


'''
#Views    
    path('users/', views.UserAPIView.as_view),
    path('accountables/', views.get_accountables),
    path('addresses/', views.get_address),
    path('attendences/', views.get_attendences),
    path('institutions/', views.get_institutions),
    path('phones/users/', views.get_phones_users),
    path('phones/institutions/', views.get_phones_institutions),

     path('voluntaries/', views.get_voluntaries),
'''