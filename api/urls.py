from django.urls import path

from api.views import *

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title='Exec API',
        default_version='1.0.0',
        description='API documentation of App'
    ),
    public=True
)
urlpatterns = [
    path('accountables/', AccountableAPIView, name='accountables'),
    path('addresses/', AddressAPIView, name='addresses'),
    path('attendences/', AttendenceAPIView, name='attendences'),
    path('institutions/', InstitutionAPIView, name='institutions'),
    path('phones/users/', PhoneUserAPIView, name='phones/users'),
    path('phones/institutions/', PhoneInstitutionAPIView, name='phones/institutions'),
    path('users/', UserAPIView, name='users'),
    path('voluntaries/', VoluntaryAPIView, name='voluntaries'),

    #Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema')
]
