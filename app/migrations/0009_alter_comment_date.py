# Generated by Django 5.2 on 2025-04-15 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_blog_image_alter_comment_author_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2025, 4, 15, 19, 6, 40, 120822), verbose_name='Дата комментария'),
        ),
    ]
