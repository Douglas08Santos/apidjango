from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import *
from api.serializers import *

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, action

from django.utils.decorators import method_decorator

from rest_framework import authentication, permissions

authentication_classes = [authentication.TokenAuthentication, ]
permission_classes = [permissions.IsAuthenticated, ]
'''
# Address
# Attendence
# Institution
# PhoneInstitution
# PhoneUser
# Voluntary
'''
# Create your views here.

# Accountable
accountable_response = openapi.Response('response description', AccountableSerializer)
class AccountableAPIView(APIView):
    @swagger_auto_schema(method='get', manual_parameters=[], responses={200: accountable_response})
    @action(detail=True, methods=['GET', 'POST'])
    def get(self, request):
        accountables = Accountable.objects.all()
        serializer = AccountableSerializer(accountables, many=True)
        return Response(serializer.data)


# Address
address_response = openapi.Response('response description', AddressSerializer)
class AddressAPIView(APIView):
    @swagger_auto_schema(method='get', manual_parameters=[], responses={200: address_response})
    @action(detail=True, methods=['GET', 'POST'])
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(method='post', manual_parameters=[], responses={200: address_response})
    @action(detail=True, methods=['POST'])
    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Attendence
attendence_response = openapi.Response('response description', AttendenceSerializer)
class AttendenceAPIView(APIView):
    @swagger_auto_schema(method='get', manual_parameters=[], responses={200: attendence_response})
    @action(detail=True, methods=['GET', 'POST'])
    def get(self, request):
        attendences = Attendence.objects.all()
        serializer = AttendenceSerializer(attendences, many=True)
        return Response(serializer.data)


# Institution
institution_response = openapi.Response('response description', InstitutionSerializer)
class InstitutionAPIView(APIView):
    @swagger_auto_schema(method='get', manual_parameters=[], responses={200: institution_response})
    @action(detail=True, methods=['GET', 'POST'])
    def get(self, request):
        institutions = Institution.objects.all()
        serializer = InstitutionSerializer(institutions, many=True)
        return Response(serializer.data)


# PhoneInstitution
phoneInstitution_response = openapi.Response('response description', PhoneInstitutionSerializer)
class PhoneInstitutionAPIView(APIView):
    @swagger_auto_schema(method='get', manual_parameters=[], responses={200: phoneInstitution_response})
    @action(detail=True, methods=['GET', 'POST'])
    def get(self, request):
        phoneInstituions = PhoneInstitution.objects.all()
        serializer = PhoneInstitutionSerializer(phoneInstituions, many=True)
        return Response(serializer.data)


# PhoneUser
phoneUser_response = openapi.Response('response description', PhoneUserSerializer)
class PhoneUserAPIView(APIView):
    @swagger_auto_schema(method='get', manual_parameters=[], responses={200: phoneUser_response})
    @action(detail=True, methods=['GET', 'POST'])
    def get(self, request):
        phoneUsers = PhoneUser.objects.all()
        serializer = PhoneUserSerializer(phoneUsers, many=True)
        return Response(serializer.data)


# User
user_response = openapi.Response('response description', UserSerializer)
class UserAPIView(APIView):
    @swagger_auto_schema(method='get', manual_parameters=[], responses={200: user_response})
    @action(detail=True, methods=['GET','POST'])
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


# Voluntary
voluntary_response = openapi.Response('response description', VoluntarySerializer)
class VoluntaryAPIView(APIView):
    @swagger_auto_schema(method='get', manual_parameters=[], responses={200: voluntary_response})
    @action(detail=True, methods=['GET', 'POST'])
    def get(self, request):
        voluntaries = Voluntary.objects.all()
        serializer = VoluntarySerializer(voluntaries, many=True)
        return Response(serializer.data)




