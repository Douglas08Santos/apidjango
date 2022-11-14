# Generated by Django 4.1.3 on 2022-11-13 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('execapi', '0004_alter_user_options_alter_phone_unique_together_and_more'),
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
        migrations.AddField(
            model_name='user',
            name='Telefones',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='execapi.phone'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='phones',
        ),
    ]
