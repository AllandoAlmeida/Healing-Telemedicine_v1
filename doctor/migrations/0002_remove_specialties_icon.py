# Generated by Django 5.0.4 on 2024-04-21 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialties',
            name='icon',
        ),
    ]
