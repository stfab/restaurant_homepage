# Generated by Django 2.2 on 2019-10-02 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_homepage', '0002_auto_20191003_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='index',
            field=models.BooleanField(default=False),
        ),
    ]