# Generated by Django 5.0.6 on 2024-07-22 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 7, 22, 13, 25, 49, 566709)),
            preserve_default=False,
        ),
    ]
