# Generated by Django 4.1.6 on 2023-03-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0003_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]