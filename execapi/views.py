from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.generic import ListView
from .models import *
import json
# Create your views here.

#Return all accountables
def get_accountables(request):
    if request.method == 'GET':
        data = list(Accountable.objects.values())
        return JsonResponse(data, safe=False)

#Return all address
def get_address(request):
    if request.method == 'GET':
        data = list(Address.objects.values())
        return JsonResponse(data, safe=False)

#Return all attendences
def get_attendences(request):
    if request.method == 'GET':
        data = list(Attendence.objects.values())
        return JsonResponse(data, safe=False)

#Return all institutions
def get_institutions(request):
    if request.method == 'GET':
        data = list(Institution.objects.values())
        return JsonResponse(data, safe=False)

#Return all phones users
def get_phones_users(request):
    if request.method == 'GET':
        data = list(PhoneUser.objects.values())
        return JsonResponse(data, safe=False)

#Return all phones institutions
def get_phones_institutions(request):
    if request.method == 'GET':
        data = list(PhoneInstitution.objects.values())
        return JsonResponse(data, safe=False)

#Return all users
def get_users(request):
    if request.method == 'GET':
        data = list(User.objects.values())
        return JsonResponse(data, safe=False)

#Return all voluntaries
def get_voluntaries(request):
    if request.method == 'GET':
        data = list(Institution.objects.values())
        return JsonResponse(data, safe=False)



    
        
   

