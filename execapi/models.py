'''

    TODO: user escolaridade
'''

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Base models
class Address(models.Model):
    street = models.CharField(max_length=100, default='')
    number = models.IntegerField(default=0)
    district = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    zip = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=50, default='')
    lat = models.CharField(max_length=20, default='')
    long = models.CharField(max_length=20, default='')

    def __str__(self):
        return '{}, {} - {}/{}'.format(self.street, self.number, self.city, self.state)

    class Meta:
        verbose_name_plural = 'Addresses'


class User(AbstractUser):
    is_voluntary = models.BooleanField('is voluntary', default=False)
    is_accountable = models.BooleanField('is accountable', default=False)
    national_id = models.CharField(max_length=14, default='')


class Phone(models.Model):
    phone = models.CharField(max_length=15, default='')
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.phone

class Institution(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')

class Voluntary(models.Model):
    #One-to-One with User
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    time_penalty = models.IntegerField(default=0)
    total_time_hours_work = models.IntegerField(default=0)
    completed_hours = models.IntegerField(default=0)
    is_employed = models.BooleanField(default=False)
    comments = models.TextField(max_length=200, default='')
    #One-to-many institution-Voluntary
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Voluntaries'


class Accountable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True)


class Attendence(models.Model):
    voluntary = models.ForeignKey(Voluntary, on_delete=models.CASCADE, null=True)
    input_time = models.DateTimeField()
    input_photo = models.ImageField()
    output_time = models.DateTimeField()
    output_photo = models.ImageField()
    is_checked = models.BooleanField()
    # TODO: Adicionar alguma biblioteca para trabalhar com latitude e longitude
    latitude = models.CharField(max_length=15, default='')
    longitude = models.CharField(max_length=15, default='')
    commments = models.TextField(max_length=200)
    


