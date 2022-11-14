from django.urls import path

from execapi.views import *

urlpatterns = [
    path('accountables/', AccountableAPIView.as_view(), name='accountables'),
    path('addresses/', AddressAPIView.as_view(), name='addresses'),
    path('attendences/', AttendenceAPIView.as_view(), name='attendences'),
    path('institutions/', InstitutionAPIView.as_view(), name='institutions'),
    path('phones/users/', PhoneUserAPIView.as_view(), name='phones/users'),
    path('phones/institutions/', PhoneInstitutionAPIView.as_view(), name='phones/institution'),
    path('users/', UserAPIView.as_view(), name='users'),
    path('voluntaries/', VoluntaryAPIView.as_view(), name='voluntaries'),
]
