# Generated by Django 4.1.3 on 2022-11-13 06:59

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_voluntary', models.BooleanField(default=False, verbose_name='is voluntary')),
                ('is_accountable', models.BooleanField(default=False, verbose_name='is accountable')),
                ('national_id', models.CharField(default='', max_length=14)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(default='', max_length=100)),
                ('number', models.IntegerField(default=0)),
                ('district', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('zip', models.CharField(default='', max_length=20)),
                ('state', models.CharField(default='', max_length=50)),
                ('lat', models.CharField(default='', max_length=20)),
                ('long', models.CharField(default='', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Voluntary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_penalty', models.IntegerField(default=0)),
                ('total_time_hours_work', models.IntegerField(default=0)),
                ('completed_hours', models.IntegerField(default=0)),
                ('is_employed', models.BooleanField(default=False)),
                ('comments', models.TextField(default='', max_length=200)),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='execapi.institution')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Voluntaries',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='', max_length=15)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_time', models.DateTimeField()),
                ('input_photo', models.ImageField(upload_to='')),
                ('output_time', models.DateTimeField()),
                ('output_photo', models.ImageField(upload_to='')),
                ('is_checked', models.BooleanField()),
                ('latitude', models.CharField(default='', max_length=15)),
                ('longitude', models.CharField(default='', max_length=15)),
                ('commments', models.TextField(max_length=200)),
                ('voluntary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='execapi.voluntary')),
            ],
        ),
        migrations.CreateModel(
            name='Accountable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='execapi.institution')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]