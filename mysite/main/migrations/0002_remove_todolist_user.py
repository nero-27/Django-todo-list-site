# Generated by Django 4.2.4 on 2023-08-10 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='user',
        ),
    ]