# Generated by Django 3.0.5 on 2022-09-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0007_delete_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]