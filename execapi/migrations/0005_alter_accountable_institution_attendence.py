# Generated by Django 4.1.3 on 2022-11-13 06:24

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('execapi', '0004_voluntary_institution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountable',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='execapi.institution'),
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_time', models.DateTimeField()),
                ('input_photo', models.ImageField(upload_to='')),
                ('output_time', models.DateField()),
                ('output_photo', models.ImageField(upload_to='')),
                ('is_checked', models.BooleanField()),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('commments', models.TextField(max_length=200)),
                ('voluntary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='execapi.voluntary')),
            ],
        ),
    ]
