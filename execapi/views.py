from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from execapi.models import *
from execapi.serializers import *

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
class AccountableAPIView(APIView):
    def get(self, request):
        accountables = Accountable.objects.all()
        serializer = AccountableSerializer(accountables, many=True)
        return Response(serializer.data)


# Address
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
class AttendenceAPIView(APIView):
    def get(self, request):
        attendences = Attendence.objects.all()
        serializer = AttendenceSerializer(attendences, many=True)
        return Response(serializer.data)

# Institution
class InstitutionAPIView(APIView):
    def get(self, request):
        institutions = Accountable.objects.all()
        serializer = InstitutionSerializer(institutions, many=False)
        return Response(serializer.data)

# PhoneInstitution
class PhoneInstitutionAPIView(APIView):
    def get(self, request):
        phoneInstituions = PhoneInstitution.objects.all()
        serializer = PhoneInstitutionSerializer(phoneInstituions, many=True)
        return Response(serializer.data)

# PhoneUser
class PhoneUserAPIView(APIView):
    def get(self, request):
        phoneUsers = PhoneUser.objects.all()
        serializer = PhoneUserSerializer(phoneUsers, many=True)
        return Response(serializer.data)

# User
class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# Voluntary
class VoluntaryAPIView(APIView):
    def get(self, request):
        voluntaries = Voluntary.objects.all()
        serializer = VoluntarySerializer(voluntaries, many=True)
        return Response(serializer.data)





