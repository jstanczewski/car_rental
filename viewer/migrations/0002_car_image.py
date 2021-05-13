# Generated by Django 3.2.2 on 2021-05-13 17:07

import django.core.validators
from django.db import migrations, models
import viewer.models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=viewer.models.get_upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['bmp', 'jpg', 'jpeg', 'jpe', 'gif', 'tif', 'tiff', 'png'])]),
        ),
    ]