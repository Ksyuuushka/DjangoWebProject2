# Generated by Django 5.1.7 on 2025-03-14 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2025, 3, 14, 9, 49, 55, 92374), verbose_name='Дата комментария'),
        ),
    ]
