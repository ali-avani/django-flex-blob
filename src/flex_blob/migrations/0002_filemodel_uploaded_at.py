# Generated by Django 5.1.4 on 2024-12-08 22:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex_blob', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Uploaded at'),
            preserve_default=False,
        ),
    ]