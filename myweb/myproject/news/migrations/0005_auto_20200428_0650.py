# Generated by Django 3.0.5 on 2020-04-28 01:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body_txt',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='short_txt',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
