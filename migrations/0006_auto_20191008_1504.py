# Generated by Django 2.2 on 2019-10-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_homepage', '0005_auto_20191008_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]