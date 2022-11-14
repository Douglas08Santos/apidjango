from django.urls import path

from execapi.views import *

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
    path('accountables/', AccountableAPIView.as_view(), name='accountables'),
    path('addresses/', AddressAPIView.as_view(), name='addresses'),
    path('attendences/', AttendenceAPIView.as_view(), name='attendences'),
    path('institutions/', InstitutionAPIView.as_view(), name='institutions'),
    path('phones/users/', PhoneUserAPIView.as_view(), name='phones/users'),
    path('phones/institutions/', PhoneInstitutionAPIView.as_view(), name='phones/institutions'),
    path('users/', UserAPIView.as_view(), name='users'),
    path('voluntaries/', VoluntaryAPIView.as_view(), name='voluntaries'),

    #Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema')
]
