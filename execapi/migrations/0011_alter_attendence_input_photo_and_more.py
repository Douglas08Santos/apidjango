# Generated by Django 4.1.3 on 2022-11-13 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('execapi', '0010_alter_attendence_input_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='input_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='output_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]