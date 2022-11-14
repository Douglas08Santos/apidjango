'''

    TODO: user escolaridade
'''

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Base models
class Address(models.Model):
    street = models.CharField('Rua', max_length=100, default='')
    number = models.IntegerField('Numero', default=0)
    district = models.CharField('Bairro', max_length=50, default='')
    city = models.CharField('Cidade', max_length=50, default='')
    zip = models.CharField('CEP', max_length=20, default='')
    state = models.CharField('Estado', max_length=50, default='')
    lat = models.CharField('Latitude', max_length=20, default='')
    long = models.CharField('Longitude', max_length=20, default='')

    def __str__(self):
        return '{}-{}'.format(self.street, self.zip)

class Phone(models.Model):
    number = models.CharField('Numero', max_length=15, default='')
    is_active = models.BooleanField('Ativo?', default=True)


    def __str__(self):
        return self.number

class User(AbstractUser):
    is_voluntary = models.BooleanField('Voluntario', default=False)
    is_accountable = models.BooleanField('Responsavel', default=False)
    national_id = models.CharField('CPF', max_length=14, default='')
    number = models.OneToOneField(to=Phone, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ['national_id', 'number']



class Institution(models.Model):
    name = models.CharField('Nome', max_length=100, default='')
    email = models.CharField('Email', max_length=100, default='')
    number = models.ForeignKey(verbose_name='Telefone', to=Phone, on_delete=models.CASCADE, null=True)
    address = models.ForeignKey(verbose_name='Endereco',to=Address, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = [['name', 'email'], ['name', 'number'], ['name', 'address']]
    def __str__(self):
        return self.name

class Voluntary(models.Model):
    #One-to-One with User
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    #One-to-many institution-Voluntary
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True)

    time_penalty = models.IntegerField(default=0)
    completed_hours = models.IntegerField(default=0)
    comments = models.TextField(max_length=200, blank=True)
    
    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)
    
    class Meta:
        verbose_name_plural = 'Voluntaries'
        unique_together = ['user', 'institution']


class Accountable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.first_name
    class Meta:
        unique_together = ['user', 'institution']

class Attendence(models.Model):
    voluntary = models.ForeignKey(Voluntary, on_delete=models.CASCADE, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True)
    input_time = models.DateTimeField()
    input_photo = models.ImageField(null=True, blank=True)
    output_time = models.DateTimeField()
    output_photo = models.ImageField(null=True, blank=True)
    is_checked = models.BooleanField()
    # TODO: Adicionar alguma biblioteca para trabalhar com latitude e longitude
    latitude = models.CharField(max_length=15, default='')
    longitude = models.CharField(max_length=15, default='')
    commments = models.TextField(max_length=200)

    class Meta:
        unique_together = ['voluntary', 'input_time', 'output_time']
    


