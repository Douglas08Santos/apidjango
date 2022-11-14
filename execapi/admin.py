from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Accountable)
class AccountableAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'institution')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'street', 'number', 'district', 'city', 'zip','state')

@admin.register(Attendence)
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'voluntary', 'institution', 'input_time', 'is_checked')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 
        'first_name', 'last_name', 'national_id',
        'email', 'is_voluntary', 'is_accountable')

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_active')


@admin.register(Voluntary)
class VoluntaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'institution', 'time_penalty', 'completed_hours')

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'number', 'address')
