# Generated by Django 4.1.3 on 2022-11-13 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('execapi', '0003_remove_accountable_nome_accountable_institution'),
    ]

    operations = [
        migrations.AddField(
            model_name='voluntary',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='execapi.institution'),
        ),
    ]
