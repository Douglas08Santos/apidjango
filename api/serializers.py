from rest_framework import serializers

from api.models import *



# Address
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'street',
            'number',
            'district',
            'city',
            'zip',
            'state',
            'lat',
            'long'
        )



# Institution
class InstitutionSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Institution
        fields = (
            'id',
            'name',
            'email',
            'address'
        )

# PhoneInstitution
class PhoneInstitutionSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer()
    class Meta:
        model = PhoneInstitution
        fields = (
            'id',
            'number',
            'institution',
            'is_active'
        )

#User
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        #Dado sensivel
        extra_kargs = {
            'national_id': {'write_only':True},
            'email': {'write_only':True}
        }
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'national_id',
            'email',
            'is_voluntary',
            'is_accountable',
            'date_joined',
            'is_active'
        )

# PhoneUser
class PhoneUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = PhoneUser
        fields = (
            'id',
            'number',
            'user',
            'is_active'
        )

# Voluntary
class VoluntarySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    institution = InstitutionSerializer()
    class Meta:
        model = Voluntary
        fields = (
            'id',
            'user',
            'institution',
            'time_penalty',
            'completed_hours',
            'comments'
        )

# Attendence
class AttendenceSerializer(serializers.ModelSerializer):
    voluntary = VoluntarySerializer()
    institution = InstitutionSerializer()
    class Meta:
        model = Attendence
        fields = (
            'id',
            'voluntary',
            'institution',
            'input_time',
            'input_photo',
            'output_time',
            'output_photo',
            'latitude',
            'longitude',
            'commments',
            'is_checked'
        )

# Accountable
class AccountableSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    institution = InstitutionSerializer()
    class Meta:
        model = Accountable
        fields = (
            'id',
            'user',
            'institution'
        )


