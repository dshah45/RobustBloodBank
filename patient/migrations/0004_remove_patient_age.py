# Generated by Django 3.0.5 on 2022-09-27 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_auto_20220926_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
    ]
