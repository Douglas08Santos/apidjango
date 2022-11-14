from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.generic import ListView
from .models import *
import json
# Create your views here.

#Return all users
def get_users(request):
    if request.method == 'GET':
        data = list(User.objects.values())
        return JsonResponse(data, safe=False)
    
        
   

