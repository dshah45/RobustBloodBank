# Generated by Django 3.0.5 on 2022-10-07 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0006_auto_20221007_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodrequest',
            name='certificate',
        ),
    ]