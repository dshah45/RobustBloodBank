# Generated by Django 3.0.5 on 2022-10-11 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0010_donor_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='bloodgroup',
        ),
    ]
