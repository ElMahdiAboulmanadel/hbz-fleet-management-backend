# Generated by Django 4.1.1 on 2022-09-20 20:53

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_phone_userprofile_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='permis_de_conduite',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='driving_license',
            field=models.FileField(blank=True, null=True, upload_to=api.models.user_directory_path),
        ),
    ]