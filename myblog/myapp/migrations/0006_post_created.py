# Generated by Django 5.2.1 on 2025-05-13 17:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
