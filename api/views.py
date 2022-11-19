from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import *
from api.serializers import *

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

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

# test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)
#accountable_response = openapi.Response('response description', AccountableSerializer)


#@swagger_auto_schema(method='get', manual_parameters=[], responses={200: accountable_response})
@api_view(['GET', 'PUT', 'POST'])
class AccountableAPIView(APIView):
    def get(self, request):
        accountables = Accountable.objects.all()
        serializer = AccountableSerializer(accountables, many=True)
        return Response(serializer.data)


# Address
# test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)
address_response = openapi.Response('response description', AddressSerializer)


@swagger_auto_schema(method='get', manual_parameters=[], responses={200: address_response})
@api_view(['GET', 'PUT', 'POST'])
class AddressAPIView(APIView):
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Attendence
# test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)
attendence_response = openapi.Response('response description', AttendenceSerializer)


@swagger_auto_schema(method='get', manual_parameters=[], responses={200: attendence_response})
@api_view(['GET', 'PUT', 'POST'])
class AttendenceAPIView(APIView):
    def get(self, request):
        attendences = Attendence.objects.all()
        serializer = AttendenceSerializer(attendences, many=True)
        return Response(serializer.data)


# Institution
# test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)
institution_response = openapi.Response('response description', InstitutionSerializer)


@swagger_auto_schema(method='get', manual_parameters=[], responses={200: institution_response})
@api_view(['GET', 'PUT', 'POST'])
class InstitutionAPIView(APIView):
    def get(self, request):
        institutions = Institution.objects.all()
        serializer = InstitutionSerializer(institutions, many=True)
        return Response(serializer.data)


# PhoneInstitution
# test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)
phoneInstituion_response = openapi.Response('response description', PhoneInstitutionSerializer)


@swagger_auto_schema(method='get', manual_parameters=[], responses={200: phoneInstituion_response})
@api_view(['GET', 'PUT', 'POST'])
class PhoneInstitutionAPIView(APIView):
    def get(self, request):
        phoneInstituions = PhoneInstitution.objects.all()
        serializer = PhoneInstitutionSerializer(phoneInstituions, many=True)
        return Response(serializer.data)


# PhoneUser
# test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)
phoneUser_response = openapi.Response('response description', PhoneUserSerializer)


@swagger_auto_schema(method='get', manual_parameters=[], responses={200: phoneUser_response})
@api_view(['GET', 'PUT', 'POST'])
class PhoneUserAPIView(APIView):
    def get(self, request):
        phoneUsers = PhoneUser.objects.all()
        serializer = PhoneUserSerializer(phoneUsers, many=True)
        return Response(serializer.data)


# User
# test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)
user_response = openapi.Response('response description', UserSerializer)


@swagger_auto_schema(method='get', manual_parameters=[], responses={200: user_response})
@api_view(['GET', 'PUT', 'POST'])
class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


# Voluntary
# test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)
voluntary_response = openapi.Response('response description', VoluntarySerializer)


@swagger_auto_schema(method='get', manual_parameters=[], responses={200: voluntary_response})
@api_view(['GET', 'PUT', 'POST'])
class VoluntaryAPIView(APIView):
    def get(self, request):
        voluntaries = Voluntary.objects.all()
        serializer = VoluntarySerializer(voluntaries, many=True)
        return Response(serializer.data)




