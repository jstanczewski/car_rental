# Generated by Django 3.2.2 on 2021-05-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
