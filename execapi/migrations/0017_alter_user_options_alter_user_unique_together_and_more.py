# Generated by Django 4.1.3 on 2022-11-14 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('execapi', '0016_alter_address_options_alter_institution_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='user',
            name='number',
        ),
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.ManyToManyField(null=True, to='execapi.phone'),
        ),
    ]