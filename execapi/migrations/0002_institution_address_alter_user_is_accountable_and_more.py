# Generated by Django 4.1.3 on 2022-11-13 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('execapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='execapi.address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_accountable',
            field=models.BooleanField(default=False, verbose_name='Responsavel'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_voluntary',
            field=models.BooleanField(default=False, verbose_name='Voluntario'),
        ),
        migrations.AlterField(
            model_name='user',
            name='national_id',
            field=models.CharField(default='', max_length=14, verbose_name='CPF'),
        ),
        migrations.AlterUniqueTogether(
            name='accountable',
            unique_together={('user', 'institution')},
        ),
        migrations.AlterUniqueTogether(
            name='attendence',
            unique_together={('voluntary', 'input_time', 'output_time')},
        ),
        migrations.AlterUniqueTogether(
            name='phone',
            unique_together={('phone', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='voluntary',
            unique_together={('user', 'institution')},
        ),
    ]