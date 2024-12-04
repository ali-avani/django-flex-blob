# Generated by Django 5.1.3 on 2024-12-03 09:17

import flex_blob.fields
import flex_blob.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', flex_blob.fields.DynamicFileField(db_index=True, upload_to=flex_blob.models.dynamic_upload_to, verbose_name='File')),
            ],
            options={
                'verbose_name': 'Base File',
                'verbose_name_plural': 'Base Files',
            },
        ),
    ]